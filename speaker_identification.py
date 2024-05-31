from google.cloud import speech_v1 as speech

def identify_speakers(audio_path):
    client = speech.SpeechClient()
    with open(audio_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US',
        diarization_config=speech.SpeakerDiarizationConfig(
            enable_speaker_diarization=True,
            min_speaker_count=1,
            max_speaker_count=5,
        ),
    )

    response = client.recognize(config=config, audio=audio)

    speakers = {}
    for result in response.results:
        for word_info in result.alternatives[0].words:
            speaker_tag = word_info.speaker_tag
            word = word_info.word
            if speaker_tag not in speakers:
                speakers[speaker_tag] = []
            speakers[speaker_tag].append(word)

    return speakers
