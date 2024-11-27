import pyttsx3
import os
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# List of text commands to convert to audio
text_commands = [
    "Welcome back, master. Your system is now ready.",
    "Hello there! Time to get things done!",
    "Good day! Let's make today productive.",
    "All systems operational. Let's get started.",
    "Your digital assistant is online. Ready to assist.",
    "It's a great day for some coding. Let's go!",
    "Initializing startup sequence. Enjoy your session.",
    "Your workspace is now set up and ready for action.",
    "Welcome to your digital playground. Let's create something amazing.",
    "System ready. Let's conquer today's tasks."
]

# Directory to save the audio files
output_folder = "C:\\Users\\hp\\Desktop\\MP3_to_WAV\\Startup_Audios"
os.makedirs(output_folder, exist_ok=True)
timestamp = time.strftime("%Y%m%d_%H%M%S")
# Generate audio files
for i, text in enumerate(text_commands):
    output_file = os.path.join(output_folder, f"startup_message_{timestamp}.wav")
    engine.save_to_file(text, output_file)
    print(f"Created: {output_file}")

# Close the engine
engine.runAndWait()
