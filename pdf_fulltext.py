#pdf_fulltext.py
"""
Author: Addison Davis
Version: 2
Date: Dec 12 2024

Takes in a list of pdfs, determines which have readable (OCR) characters
More than 100 characters -> has OCR text

"""
import pymupdf
import requests
import math
import re

#Expects an input filename directing to a text file with a list of pdf files.
#You can create this by selecting all the pdfs in a folder and copying their filepaths to a new text file.
INPUT_FILE = ""

files = []

with open(INPUT_FILE, "r") as file:
    for line in file:
        files.append(line.strip())

count_ocr = 0

no_ocr = []

CHAR_CUTOFF = 100 # Seems like many non-OCR pdfs may still have up to 100 characters

for filename in files:
    filename = filename[1:-1] #remove leading and trailing quotation marks
    try:
        with pymupdf.open(filename) as doc:
            print(doc.get_toc())
            text = chr(12).join([page.get_text() for page in doc])
            #print(f"{filename}: {len(text)} characters")
            if len(text) > CHAR_CUTOFF: # arbitrary cutoff but seems about right
                count_ocr += 1
            else:
                no_ocr.append(re.search("\d\d\d\d\d\d", filename).group())
    except: 
        print(f"Unable to open {filename}")

print(f"No OCR:")
for tn in no_ocr: print(tn)
print(f"Complete. {count_ocr} PDFs with OCR text available out of {len(files)} delivered files ({math.floor(100*(count_ocr/len(files)))}%).")
