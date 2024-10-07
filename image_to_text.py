gemni_key = 'AIzaSyCNU-nBcSfoY5Sq0TV41kEyiiD_D2HB-34'

import google.generativeai as genai
import streamlit as st
import PIL.Image
from PIL import Image
import pytesseract

genai.configure(api_key=gemni_key)

# # Configure the path to tesseract executable (for Windows users)
# # pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract.exe'

st.title("Image to Text Converter")

# # Upload the image
uploaded_image = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

    
if st.button('Submit'):
    model = genai.GenerativeModel("gemini-1.5-flash")
    organ = PIL.Image.open(uploaded_image)
    response = model.generate_content(["Tell me about this instrument", organ])
    st.write(response.text)