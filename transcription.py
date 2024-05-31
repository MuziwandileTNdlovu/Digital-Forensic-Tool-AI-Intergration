from google.cloud import speech_v1 as speech
from pydub import AudioSegment

def format_audio_segment(audio_path):
    audio = AudioSegment.from_file(audio_path)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)
    audio_segment = audio[:59 * 1000]
    segment_path = "tempaudio/temp_segment.wav"
    audio_segment.export(segment_path, format="wav")
    return segment_path

def transcribe_audio(audio_path):
    audio_path = format_audio_segment(audio_path)
    client = speech.SpeechClient()
    with open(audio_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        # sample_rate_hertz=16000,
        language_code='en-US'
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript , audio_path
# Example usage:
# transcribed_text = transcribe_audio('path_to_audio_file.wav')
