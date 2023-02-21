import os
import re
from google.cloud import texttospeech

# Set up Google Cloud Text-to-Speech credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../burnished-road-378220-e10d29d380d2.json"

# Set up Text-to-Speech client
client = texttospeech.TextToSpeechClient()

# Define book title
book_title = "Thinking, Fast and Slow"

# Define regex pattern to match chapter title

# Loop through each file in the output directory
for filename in os.listdir("output"):

        # Read the chapter summary from the file
        with open(os.path.join("output", filename), "r") as f:
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
        with open(os.path.join("audio", f"{filename}.mp3"), "wb") as f:
            f.write(response.audio_content)