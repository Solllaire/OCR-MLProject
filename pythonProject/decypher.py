import subprocess
from PIL import Image
import pytesseract
from Source import file_name, textfile, resultfile
import os

# Source contains token, and names for 3 txt files
# Vital to create by yourself

def OCR_method(path):
    files = textfile+' '+resultfile
    text = pytesseract.image_to_string(Image.open(file_name))
    with open(textfile, "w") as text_file:
        text_file.write(text)
    os.remove(file_name)
    os.popen(f"npx echogarden detect-text-language {files}").read()
