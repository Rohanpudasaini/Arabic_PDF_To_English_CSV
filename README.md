# Philipp_Project_Python
Final product of the project.

## How to Run the Script?

* Download the sample file.
* Run all commands from ***Commands_to_run.txt***
* Import all the PDFs in ***Documents*** folder inside ***Sample*** folder
* Run ***main.py***
* All informations will be appended in ***Book-v2.csv***

## What Do this Script DO?
This script use [***poppler-utils***](https://pypi.org/project/poppler-utils/) to convert a pdf into image and
after that use tesseract-ocr and arabic tesdata to extract the text.`we run the ocr 2 times as we arabic ocr can accurately extract numeric valuse.`
