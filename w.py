from pydub import AudioSegment
from pydub.utils import which
import os
import time

def correct_path(path):
    # Remove unnecessary quotes and normalize the path
    path = path.strip('"').strip("'")
    return os.path.normpath(path)

# Set paths
AudioSegment.ffmpeg = which("ffmpeg")  # Auto-detect ffmpeg
AudioSegment.ffprobe = which("ffprobe")  # Auto-detect ffprobe

output_folder = r"C:\Users\hp\Desktop\MP3_to_WAV\WAV_FILES"
os.makedirs(output_folder, exist_ok=True)

# Get user input for the input file path
input_files = input("Enter the path of the audio/video file to convert: ")
input_file = correct_path(input_files)

# Generate unique output file name
timestamp = time.strftime("%Y%m%d_%H%M%S")
output_file = os.path.join(output_folder, f"output_{timestamp}.wav")

# Load the file and convert
try:
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="wav")
    print(f"File successfully converted and saved as {output_file}")
except FileNotFoundError:
    print("Error: The specified file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
