from llamaapi import LlamaAPI
import markdown2
import pdfkit

llama = LlamaAPI("LL-b4KliMUrQbVZvi5plKHzAUW5wYcwpz6uGNNtAFkffQukRdneinqbCPLy3sxLhzV3")

def format_report_with_llm(data):
    transcription = data['transcription']
    sentiment = data['sentiment']
    speakers = data['speakers']
    keywords_rake = data['keywords_rake']
    keywords_yake = [kw[0] for kw in data['keywords_yake']]

    speaker_segments = "\n".join(
        [f"**Speaker {speaker_id}:** {', '.join(words[1:])}" for speaker_id, words in speakers.items()]
    )

    prompt = f"""
    You are an expert in digital forensics. Based on the data provided, write a comprehensive and professional report. Explain each section in detail, including what each term means.

    ## Transcription
    This section provides the transcribed text from the audio or video data collected during the forensic analysis. It captures all spoken words verbatim.
    **Transcribed Text:** {transcription}

    ##Sentiment Analysis:
    Sentiment analysis assesses the emotional tone of the transcribed text. It provides two main metrics:
    - Polarity: Indicates the sentiment orientation (positive, neutral, or negative). Values range from -1 (very negative) to +1 (very positive).
    - Subjectivity: Measures the degree of personal opinion or bias expressed in the text. Values range from 0 (very objective) to 1 (very subjective).
    Results: Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}

    ## Speaker Identification
    Speaker identification identifies different speakers in the audio or video data and assigns labels to them. This helps in understanding who said what during the conversation.
    **Identified Speakers:**
    {speaker_segments}

    ## Keyword Extraction (RAKE)
    RAKE (Rapid Automatic Keyword Extraction) is a method to identify key phrases in the text. It helps in summarizing the main topics discussed.
    **Extracted Keywords:** {', '.join(keywords_rake)}

    ## Keyword Extraction (YAKE)
    YAKE (Yet Another Keyword Extractor) is another method for keyword extraction. It ranks keywords based on their significance within the text.
    **Extracted Keywords:** {', '.join(keywords_yake)}

    ## Detailed Report
    Based on the above analysis, provide a structured and logical report explaining the findings and their implications in the context of digital forensics.
    """

    api_request_json = {
        "model": "llama3-70b",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": "Please create that report for me with good formatting. Add the Date and A Random Case number"},
        ]
    }

    response = llama.run(api_request_json)
    response = response.json()
    return response['choices'][0]['message']['content']

def generate_pdf_report(content, output_file):
    # Convert Markdown content to HTML
    html_content = markdown2.markdown(content)
    
    # Save the HTML content to a PDF file using a tool like weasyprint or pdfkit
    pdfkit.from_string(html_content, output_file)

def create_report(data, output_file):
    report_content = format_report_with_llm(data)
    with open('report/report.md', 'w') as file:
        file.write(report_content)
    generate_pdf_report(report_content, output_file)