import pyttsx3
import os
import textwrap

# Initialize the TTS engine
engine = pyttsx3.init()

# Get all available voices
voices = engine.getProperty('voices')

# Filter Male and Female voices
male_voices = [voice for voice in voices if "male" in voice.name.lower()]
female_voices = [voice for voice in voices if "female" in voice.name.lower()]

print("\n🔹🔹🔹 *Choose the Voice for Speaking* 🔹🔹🔹")
print("1. Male Voice")
print("2. Female Voice")
choice = input("Enter your choice (1 for Male, 2 for Female): ")

# Set the selected voice
if choice == '1' and male_voices:
    engine.setProperty('voice', male_voices[0].id)
    print("✅ Male voice selected.")
elif choice == '2' and female_voices:
    engine.setProperty('voice', female_voices[0].id)
    print("✅ Female voice selected.")
else:
    print("⚠ Invalid choice or voice not available. Default voice selected.")

# Set parameters for more human-like speech
engine.setProperty('rate', 150)      # Speed of speech (Default ~200)
engine.setProperty('volume', 1.0)    # Volume level (0.0 to 1.0)

# Directory for saving files
if not os.path.exists('myrecords'):
    os.makedirs('myrecords')

# Taking user input to speak
while True:
    text = input("\n💬 Enter the text to speak (or type 'exit' to quit): ")
    if text.lower() == 'exit':
        break

    print("🎙 Speaking...")

    # *Handle Large Paragraphs:* Break text into chunks of 150 characters
    chunks = textwrap.wrap(text, width=150)

    # Speak each chunk smoothly
    for chunk in chunks:
        engine.say(chunk)
    engine.runAndWait()

    # Ask if user wants to save the audio
    save_option = input("\n💾 Do you want to save this audio? (y/n): ")
    if save_option.lower() == 'y':
        file_name = f"myrecords/recording.mp3"
        print("💾 Saving... This may take a few seconds.")
        # Save all chunks to a single file
        for chunk in chunks:
            engine.save_to_file(chunk, file_name)
        engine.runAndWait()
        print(f"✅ Audio saved as {file_name}")