# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
openai.api_key="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"
audio_file= open("/home/berk/Desktop/bitirme/bitirme/test.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)