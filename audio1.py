import streamlit as st
from gtts import gTTS
import os
from datetime import datetime

# Set up Streamlit UI
st.title("🗣 Text-to-Speech Application")
st.write("Enter the text you want to convert to speech:")

# Text input
text = st.text_area("💬 Enter your text here:")

# Voice selection (gTTS supports only one type of voice for now)
voice_choice = st.radio("Choose Voice Type:", ('Male (Default)', 'Female (Default)'))

# Save directory
if not os.path.exists('myrecords'):
    os.makedirs('myrecords')

# Action buttons
if st.button("🔊 Speak"):
    st.write("🎙 Speaking...")
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    st.audio("temp.mp3")
    st.success("✅ Speech completed.")

if st.button("💾 Save & Download Audio"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"myrecords/recording_{timestamp}.mp3"
    tts.save(file_name)
    st.success(f"✅ Audio saved as {file_name}")
    
    # Show download button
    with open(file_name, "rb") as audio_file:
        st.download_button(label="⬇ Download Audio", 
                           data=audio_file, 
                           file_name=f"recording_{timestamp}.mp3",
                           mime='audio/mp3')
