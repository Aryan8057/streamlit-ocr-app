import pytesseract
from PIL import Image
import streamlit as st

# OCR function with error handling
def process_image(image):
    try:
        extracted_text = pytesseract.image_to_string(image, lang="hin+eng")
        if not extracted_text.strip():
            return "No text found in the image. Please try another image."
        return extracted_text
    except Exception as e:
        return f"Error during OCR: {str(e)}"

# Keyword search function
def search_keywords(text, keyword):
    try:
        if keyword.lower() in text.lower():
            return f'Keyword "{keyword}" found!'
        return f'Keyword "{keyword}" not found.'
    except Exception as e:
        return f"Error during search: {str(e)}"

# Streamlit app layout
st.title("Hindi and English OCR with Keyword Search")

# Upload an image
uploaded_image = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

# Input for keyword search
keyword = st.text_input("Enter Keyword to Search")

# If image is uploaded and keyword is entered
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    extracted_text = process_image(image)

    st.subheader("Extracted Text")
    st.text(extracted_text)

    if keyword:
        search_result = search_keywords(extracted_text, keyword)
        st.subheader("Search Result")
        st.text(search_result)


## Attempt 2
# import pytesseract
# from PIL import Image
# import streamlit as st
# import os

# # (Optional) Set the path for the Tesseract executable (only for Windows)
# # For Linux/Ubuntu environments, remove the next line.
# # pytesseract.pytesseract.tesseract_cmd = r"C://Program Files//Tesseract-OCR//tesseract.exe"

# # OCR function with error handling
# def process_image(image):
#     try:
#         # Use Tesseract for both Hindi and English languages
#         config = '--oem 3 --psm 6'
#         extracted_text = pytesseract.image_to_string(image, lang="hin+eng")
#         if not extracted_text.strip():
#             return "No text found in the image. Please try another image."
#         return extracted_text
#     except Exception as e:
#         return f"Error during OCR: {str(e)}"

# # Keyword search function
# def search_keywords(text, keyword):
#     try:
#         if keyword.lower() in text.lower():
#             return f'Keyword "{keyword}" found!'
#         return f'Keyword "{keyword}" not found.'
#     except Exception as e:
#         return f"Error during search: {str(e)}"

# # Streamlit app layout
# st.title("Hindi and English OCR with Keyword Search")

# # Upload an image
# uploaded_image = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

# # Input for keyword search
# keyword = st.text_input("Enter Keyword to Search")

# # If image is uploaded and keyword is entered
# if uploaded_image is not None:
#     image = Image.open(uploaded_image)

#     # Process the uploaded image
#     extracted_text = process_image(image)

#     # Display the extracted text
#     st.subheader("Extracted Text")
#     st.text(extracted_text)

#     # If the keyword is provided, search in the extracted text
#     if keyword:
#         search_result = search_keywords(extracted_text, keyword)
#         st.subheader("Search Result")
#         st.text(search_result)


## Attempt 3
# import pytesseract
# from PIL import Image
# import streamlit as st
# import cv2
# import numpy as np
# from PIL import Image, ImageFilter, ImageOps

# # (Optional) Set the path for the Tesseract executable (only for Windows)
# # pytesseract.pytesseract.tesseract_cmd = r"C://Program Files//Tesseract-OCR//tesseract.exe"

# # OCR function with error handling
# def process_image(image):
#     try:
#         # Convert to grayscale
#         image = image.convert('L')
        
#         # Apply thresholding
#         image = image.point(lambda x: 0 if x < 128 else 255, '1')
        
#         # Apply sharpening filter
#         image = image.filter(ImageFilter.SHARPEN)
        
#         extracted_text = pytesseract.image_to_string(image, lang="hin+eng", config='--oem 1')
#         if not extracted_text.strip():
#             return "No text found in the image. Please try another image."
#         return extracted_text
#     except Exception as e:
#         return f"Error during OCR: {str(e)}"


# # Keyword search function
# def search_keywords(text, keyword):
#     try:
#         if keyword.lower() in text.lower():
#             return f'Keyword "{keyword}" found!'
#         return f'Keyword "{keyword}" not found.'
#     except Exception as e:
#         return f"Error during search: {str(e)}"

# # Streamlit app layout
# st.title("Hindi and English OCR with Keyword Search")

# # Upload an image
# uploaded_image = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

# # Input for keyword search
# keyword = st.text_input("Enter Keyword to Search")

# # If image is uploaded and keyword is entered
# if uploaded_image is not None:
#     image = Image.open(uploaded_image)

#     # Process the uploaded image
#     extracted_text = process_image(image)

#     # Display the extracted text
#     st.subheader("Extracted Text")
#     st.text(extracted_text)

#     # If the keyword is provided, search in the extracted text
#     if keyword:
#         search_result = search_keywords(extracted_text, keyword)
#         st.subheader("Search Result")
#         st.text(search_result)



## Attempt 4
# import pytesseract
# from PIL import Image, ImageFilter
# import streamlit as st

# # Set Tesseract OCR path if needed
# # pytesseract.pytesseract.tesseract_cmd = "C://Program Files//Tesseract-OCR//tesseract.exe"

# # OCR function with image preprocessing
# def process_image(image):
#     try:
#         # Convert to grayscale
#         image = image.convert('L')
        
#         # Optional: Apply image filtering (sharpness, contrast, etc.)
#         image = image.filter(ImageFilter.SHARPEN)
        
#         # Binarization using adaptive thresholding
#         image = image.point(lambda x: 0 if x < 128 else 255, '1')
        
#         # Extract text using Tesseract
#         extracted_text = pytesseract.image_to_string(image, lang="hin+eng", config='--oem 3 --psm 6')
        
#         if not extracted_text.strip():
#             return "No text found in the image. Please try another image."
#         return extracted_text
#     except Exception as e:
#         return f"Error during OCR: {str(e)}"

# # Keyword search function
# def search_keywords(text, keyword):
#     try:
#         if keyword.lower() in text.lower():
#             return f'Keyword "{keyword}" found!'
#         return f'Keyword "{keyword}" not found.'
#     except Exception as e:
#         return f"Error during search: {str(e)}"

# # Streamlit app layout
# st.title("Hindi and English OCR with Keyword Search")

# # Upload an image
# uploaded_image = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

# # Input for keyword search
# keyword = st.text_input("Enter Keyword to Search")

# # If image is uploaded and keyword is entered
# if uploaded_image is not None:
#     image = Image.open(uploaded_image)
#     extracted_text = process_image(image)

#     st.subheader("Extracted Text")
#     st.text(extracted_text)

#     if keyword:
#         search_result = search_keywords(extracted_text, keyword)
#         st.subheader("Search Result")
#         st.text(search_result)


## Attempt 5
# import gradio as gr
# import pytesseract
# from PIL import Image, ImageFilter
# import os

# # Set path for Tesseract executable (modify based on your setup)
# # pytesseract.pytesseract.tesseract_cmd = "C://Program Files//Tesseract-OCR//tesseract.exe"

# # OCR function with preprocessing
# def process_image(image):
#     try:
#         # Convert to grayscale
#         image = image.convert('L')
        
#         # Optional: Apply image filtering
#         image = image.filter(ImageFilter.SHARPEN)
        
#         # Binarization
#         image = image.point(lambda x: 0 if x < 128 else 255, '1')
        
#         # Extract text
#         extracted_text = pytesseract.image_to_string(image, lang="hin+eng")
        
#         if not extracted_text.strip():
#             return "No text found in the image. Please try another image."
#         return extracted_text
#     except Exception as e:
#         return f"Error during OCR: {str(e)}"

# # Keyword search function
# def search_keywords(text, keyword):
#     try:
#         if keyword.lower() in text.lower():
#             return f'Keyword "{keyword}" found!'
#         return f'Keyword "{keyword}" not found.'
#     except Exception as e:
#         return f"Error during search: {str(e)}"

# # Main function for OCR and keyword search
# def ocr_app(image, keyword):
#     extracted_text = process_image(image)
#     search_result = search_keywords(extracted_text, keyword)
#     return extracted_text, search_result

# # Gradio interface
# iface = gr.Interface(
#     fn=ocr_app,
#     inputs=[
#         gr.Image(type="pil", label="Upload Image"),
#         gr.Textbox(label="Enter Keyword to Search")
#     ],
#     outputs=[
#         gr.Textbox(label="Extracted Text"),
#         gr.Textbox(label="Search Result")
#     ],
#     title="Hindi and English OCR with Keyword Search"
# )

# # Launch the app
# iface.launch(debug=True)
