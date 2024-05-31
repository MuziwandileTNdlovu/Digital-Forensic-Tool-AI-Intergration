from transcription import transcribe_audio
from sentiment_analysis import perform_sentiment_analysis
from speaker_identification import identify_speakers
from keyword_extraction import extract_keywords_rake, extract_keywords_yake
from generate_report import create_report
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secrets/cos783-project-3f3bc31da814.json'

def process_audio(file_path):
    transcribed_text , audio_path = transcribe_audio(file_path)
    sentiment = perform_sentiment_analysis(transcribed_text)
    speakers = identify_speakers(audio_path)
    keywords_rake = extract_keywords_rake(transcribed_text)
    keywords_yake = extract_keywords_yake(transcribed_text)
    
    return {
        'transcription': transcribed_text,
        'sentiment': sentiment,
        'speakers': speakers,
        'keywords_rake': keywords_rake,
        'keywords_yake': keywords_yake
    }

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Process an audio file for transcription, sentiment analysis, speaker identification, and keyword extraction.")
    parser.add_argument("file_path", type=str, help="Path to the audio file to be processed.")
    
    args = parser.parse_args()
    
    result = process_audio(args.file_path)

    create_report(result, 'reports/report.pdf')


    print("Transcription:")
    print(result['transcription'])
    print("\nSentiment Analysis:")
    print(result['sentiment'])
    print("\nSpeaker Identification (Flags, Classes):")
    print(result['speakers'])
    print("\nKeywords (RAKE):")
    print(result['keywords_rake'])
    print("\nKeywords (YAKE):")
    print(result['keywords_yake'])
