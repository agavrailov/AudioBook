import os
import re
from google.cloud import texttospeech

# Set up Google Cloud Text-to-Speech credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../burnished-road-378220-e10d29d380d2.json"

# Set up Text-to-Speech client
client = texttospeech.TextToSpeechClient()

# Read the chapter summary from the file
with open("output/all.txt", "r") as f:
    summary = f.read().strip()

# Set up Text-to-Speech request
synthesis_input = texttospeech.SynthesisInput(text=summary)
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Neural2-D",
    ssml_gender=texttospeech.SsmlVoiceGender.MALE,
)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.OGG_OPUS,
)

request = texttospeech.SynthesizeSpeechRequest(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# Generate the speech and save to file
response = client.synthesize_speech(request=request)
with open("/audio", "all.mp3") as f:
    f.write(response.audio_content)