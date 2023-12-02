# -*- coding: utf-8 -*-
"""
Created on Nov 2023

@author: Angelos
"""

import pyttsx3
from PyPDF2 import PdfReader

# Insert the path to your PDF file
pdf_path = 'D:/folder/pdf file name.pdf'

# Create a PdfReader object
pdf_reader = PdfReader(pdf_path)

# Initialize the text variable
text = ""

# Extract text from each page
for page_num in range(len(pdf_reader.pages)):
    text += pdf_reader.pages[page_num].extract_text()

# Clean up the text
clean_text = text.strip().replace('\n', ' ')
print(clean_text)

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Save the text to an MP3 file
mp3_path = 'D:/folder/mp3 file name.mp3'
speaker.save_to_file(clean_text, mp3_path)
speaker.runAndWait()

speaker.stop()
