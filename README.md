# Png-to-Clipboard

##🤧 Tired of writing all the text because the site doesn't let you use control+c to copy the text?

This repository contains a Python script developed as a practical application of concepts related to file handling, image processing, and Optical Character Recognition (OCR). The main goal of this project is to automate the extraction of text from screenshots and copy it directly to the clipboard, providing a streamlined workflow for users who frequently need to capture and utilize text from images.

##📸 About the Project

The Screenshot Text Extractor script continuously monitors a designated folder (by default, ~/Desktop/Screenshots) for new PNG screenshots. Once a new screenshot is detected, the script performs OCR to extract any text present in the image and copies the extracted text to the clipboard. This automation saves time and simplifies the process of transferring text from images to other applications.

##Key Features:
Automatic Detection: Real-time monitoring of a specified folder for new screenshots.
OCR Text Extraction: Uses pytesseract to convert text from images into editable text.
Clipboard Integration: Automatically copies extracted text to the clipboard for easy access.
User-Friendly: Simple setup and seamless integration into your daily workflow.

##💻 Technologies Used

Programming Language: Python
Libraries: Pillow for image handling, pytesseract for text recognition, and pyperclip for clipboard management.
External Dependency: tesseract-ocr (must be installed separately for OCR functionality).

##📚 Learning Outcomes and Challenges

File Handling: Understanding how to monitor directories and manage file operations.
Image Processing: Utilizing image libraries to read and process image files.
OCR Implementation: Applying pytesseract for text extraction and handling various OCR challenges.
Clipboard Automation: Using pyperclip to interact with the system clipboard.
This project was a great opportunity to practice integrating multiple Python libraries to automate tasks, improve workflow efficiency, and solve practical problems. It also provided valuable experience in real-time event handling and continuous monitoring within a Python environment.
