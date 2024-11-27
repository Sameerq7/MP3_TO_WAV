# from pydub import AudioSegment
# from pydub.utils import which

# AudioSegment.ffmpeg = which("ffmpeg")
# AudioSegment.ffprobe = which("ffprobe")

# print("FFmpeg Path:", AudioSegment.ffmpeg)
# print("FFprobe Path:", AudioSegment.ffprobe)

# mp3_path = r"C:\Users\hp\Desktop\nextapp\ElevenLabs_2024-09-13T16_48_03_Adam_pre_s69_sb92_se0_b_m2.mp3"

# try:
#     audio = AudioSegment.from_mp3(mp3_path)
#     audio.export("output3.wav", format="wav")
#     print("Conversion successful!")
# except Exception as e:
#     print("An error occurred:", e)
#.\.venv\Scripts\activate
from pydub import AudioSegment
from pydub.utils import which
import os
import time
import subprocess
import sys

env_activate = os.path.join(".venv", "Scripts", "activate")

# This part won't work to activate the environment in the current script.
# It's better to ensure the environment is already activated before running this script.
# Uncomment the following line if you want to try it, but it's not recommended.
# subprocess.call(env_activate, shell=True)

# Set paths
ffmpeg_path = r"C:\ffmpeg\ffmpeg.exe"
ffprobe_path = r"C:\ffmpeg\ffprobe.exe"
output_folder = r"C:\Users\hp\Desktop\MP3_to_WAV\WAV_FILES"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get user input for the input file path
input_file = input("Enter the path of the audio/video file to convert: ")

# Normalize the path for Windows
input_file = os.path.abspath(input_file).replace("/", "\\")

# Generate unique output file name
timestamp = time.strftime("%Y%m%d_%H%M%S")
output_file = os.path.join(output_folder, f"output_{timestamp}.wav")

# Set ffmpeg and ffprobe paths for pydub
AudioSegment.ffmpeg = ffmpeg_path
AudioSegment.ffprobe = ffprobe_path

# Load the file and convert
try:
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="wav")
    print(f"File successfully converted and saved as {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")
