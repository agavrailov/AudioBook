import os
from pydub import AudioSegment

# Path to output directory where the chapter files are saved
input_dir = "audio"

# Get list of all mp3 files in the output directory
mp3_files = [f for f in os.listdir(input_dir) if f.endswith(".mp3")]

# Sort the list of mp3 files by name
mp3_files.sort()

# Create an empty audio segment to store the concatenated audio
full_audio = AudioSegment.empty()

# Concatenate all the mp3 files into one audio segment
for mp3_file in mp3_files:
    chapter_audio = AudioSegment.from_file(os.path.join(input_dir, mp3_file), format="mp3")
    full_audio += chapter_audio

# Save the full book audio to a file
full_audio.export("full_book.mp3", format="mp3")
