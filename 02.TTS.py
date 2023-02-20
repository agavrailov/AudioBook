from google.cloud import texttospeech
import os

# Define book title and chapter names
book_title = "Thinking, Fast and Slow"
chapter_names = ["Chapter 1", "Chapter 2", "Chapter 3", ... "Chapter 39"]

# Set up Google Cloud Text-to-Speech client and voice options
client = texttospeech.TextToSpeechClient()
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", name="en-US-Wavenet-D", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

# Loop through each chapter and generate audio file using Google Cloud Text-to-Speech
for chapter_name in chapter_names:
    # Define input and output file names
    input_filename = f"{chapter_name}.txt"
    output_filename = f"{chapter_name}.mp3"
    # Load input text file
    with open(input_filename, "r") as f:
        text = f.read().replace("\n", " ")
    # Set up and execute synthesis request
    synthesis_input = texttospeech.SynthesisInput(text=text)
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    # Save audio file
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)
