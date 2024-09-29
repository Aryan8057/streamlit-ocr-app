# streamlit-ocr-app

# Hindi and English OCR with Keyword Search

## Project Overview

This project is a web application built using Streamlit that utilizes Tesseract OCR to extract text from images containing Hindi and English text. Users can upload an image and search for specific keywords within the extracted text. The application is designed to be user-friendly and efficient, enabling quick text extraction and keyword search.

## Features

- Upload images in PNG, JPG, or JPEG format.
- Extract text from uploaded images using Tesseract OCR.
- Search for specific keywords within the extracted text.
- Display extracted text and search results in a clear format.

## Technologies Used

- **Python 3.9.7**
- **Streamlit 1.12.0**: For creating the web interface.
- **Pillow**: For image processing.
- **pytesseract**: For optical character recognition (OCR).
- **Tesseract OCR**: Open-source OCR engine for extracting text.

## Installation

### Prerequisites

- Python 3.9.x
- Tesseract OCR installed on your system.

### Clone the Repository
```
git clone https://github.com/Aryan8057/streamlit-ocr-app.git
cd streamlit-ocr-app
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Create a requirements.txt file and add the following dependencies:
streamlit==1.12.0
pytesseract==0.3.13
Pillow==8.4.0

Then run:
pip install -r requirements.txt

Tesseract Installation
Linux: Install Tesseract via your package manager. For example:
sudo apt install tesseract-ocr tesseract-ocr-hin

Windows: Download the Tesseract installer from Tesseract at UB Mannheim and follow the installation instructions.

Usage
Run the Streamlit app:
streamlit run app.py
Open your browser and navigate to http://localhost:8501.
Upload an image containing Hindi and/or English text.
Enter a keyword to search for within the extracted text.
View the extracted text and search results.


Example
Here’s an example of how to use the app:
Upload an image containing text.
Enter a keyword, such as "Hello" or "नमस्ते".
View the extracted text and whether the keyword was found.

Contributions are welcome! Please feel free to open an issue or submit a pull request.


Acknowledgments
Tesseract OCR for providing the OCR capabilities.
Streamlit for creating an easy-to-use web interface.
