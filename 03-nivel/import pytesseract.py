import pytesseract
import pyautogui
from PIL import Image
import cv2
import numpy as np

# Set the tesseract executable path if you're on Windows
# For example:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_screen(region=None):
    """
    Captures a screenshot of the entire screen or a specific region.
    
    Parameters:
    region: A tuple (left, top, width, height) to specify the region to capture.
    
    Returns:
    Image object (PIL format)
    """
    screenshot = pyautogui.screenshot(region=region)
    return screenshot

def preprocess_image(image):
    """
    Preprocess the image to improve OCR accuracy.
    
    Parameters:
    image: The PIL Image to preprocess.
    
    Returns:
    Processed image in OpenCV format.
    """
    # Convert the image to grayscale
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to make text stand out
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    return thresh

def ocr_image(image):
    """
    Perform OCR on the given image.
    
    Parameters:
    image: The image (PIL or OpenCV format) to extract text from.
    
    Returns:
    Extracted text as a string.
    """
    text = pytesseract.image_to_string(image)
    return text

# Main function to capture, process, and perform OCR
def capture_and_extract_text(region=None):
    # Step 1: Capture the screen (entire screen or specific region)
    captured_image = capture_screen(region)
    
    # Step 2: Preprocess the image for better OCR accuracy
    processed_image = preprocess_image(captured_image)
    
    # Step 3: Perform OCR on the processed image
    extracted_text = ocr_image(processed_image)
    
    return extracted_text

# Example usage:
if __name__ == "__main__":
    # Optionally, specify a region to capture (left, top, width, height)
    # For example, capturing the upper-left part of the screen (100, 100) with width 800 and height 600
    region = (100, 100, 800, 600)  # Adjust this as necessary
    
    # Capture and extract text
    text = capture_and_extract_text(region)
    
    # Output the extracted text
    print("Extracted Text:\n", text)
