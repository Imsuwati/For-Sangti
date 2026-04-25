import streamlit as st
import os
from PIL import Image

# 1. Set up the page design
st.set_page_config(page_title="For Sangti ❤️", page_icon="💌", layout="centered")

# Trigger an animation of balloons when she opens it!
st.balloons()

# 2. The Header Section
st.title("To My Amazing And Wonderful Lady 💖")
st.subheader("A little something I built just for you...")
st.write("---") 

# 3. Your Sweet Message
st.write("Sangti, I just wanted to take a moment to thank you for always being such a good girl. You bring so much joy, peace, and warmth into my life, and I appreciate everything you do.")
st.write("You are my favorite person, my biggest supporter, and my best friend. Every single day with you feels like a gift. Thank you for being exactly who you are.")
st.write("---")

# 4. The Photo Gallery
st.header("Some of My Favorite Pictures 📸")

# A smart helper function to find your pictures automatically
def find_my_picture(filename):
    # It will check for all three common image types
    for extension in [".jpg", ".jpeg", ".png"]:
        if os.path.exists(filename + extension):
            return Image.open(filename + extension)
    return None

# Create two columns to put pictures side-by-side
col1, col2 = st.columns(2)

with col1:
    img1 = find_my_picture("pics1")
    if img1:
        st.image(img1, caption="Your beautiful Face", use_container_width=True)
    else:
        st.error("Error: Python cannot find pics1 in this folder.")

with col2:
    img2 = find_my_picture("pics2")
    if img2:
        st.image(img2, caption="You make everything better", use_container_width=True)
    else:
        st.error("Error: Python cannot find pics2 in this folder.")

st.write("---")

# 5. The Grand Finale
st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>I love you so much my baby Sangti 💌</h2>", unsafe_allow_html=True)