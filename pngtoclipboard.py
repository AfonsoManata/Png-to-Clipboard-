import os
from PIL import Image
import pytesseract
import pyperclip
import time

# Set the path to the folder that is receiving your screenshots
screenshot_folder = os.path.expanduser("~/Desktop/Screenshots") 
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

def delete_all_screenshots():
    
    # Iterating in the screenshots folder
    for f in os.listdir(screenshot_folder):
    
        # If is a screenshot (and not a video)
        if f.endswith(".png"):
            
            # Remove the screenshot 
            try:
                os.remove(os.path.join(screenshot_folder, f))
            
            # Exception
            except Exception as e:
                print(f"Failed to delete {f}: {e}")

def get_latest_screenshot():
    
    # List all PNG files in the screenshots folder
    files = [f for f in os.listdir(screenshot_folder) if f.endswith('.png')]
    
    if not files: return None
    
    # Get the full paths of all the files
    full_paths = [os.path.join(screenshot_folder, f) for f in files]
    
    # Find the most recent file 
    latest_file = max(full_paths, key = os.path.getctime)
    
    return latest_file

def extract_text_from_image(image_path):
    
    try:
        # Open the image and use pytesseract to extract text
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image) 
        return text
    
    except Exception as e:
        
        print(f"Error extracting text from image: {e}")
        return ""

def main():
    
    seen_files = set()  
    print("Monitoring for new screenshots. Press Ctrl+C to exit.")
    try:
        while True:
            
            # Get the most recent screenshot
            screenshot_path = get_latest_screenshot()
            
            if screenshot_path and screenshot_path not in seen_files:
                
                # Turn this file to a seen file
                seen_files.add(screenshot_path)  
                
                print(f"Processing screenshot: {screenshot_path}")
                text = extract_text_from_image(screenshot_path)
                
                if text.strip():
                    # Copy the text to the clipboard
                    pyperclip.copy(text.strip())
                    print("Text copied to clipboard!")
                
                else:
                    print("No text found in the screenshot.")
            time.sleep(0.1)

    except KeyboardInterrupt:
        delete_all_screenshots()
        print("\nExiting the program.")


# This will run only if the script is executed directly
if __name__ == "__main__":
    main() 


