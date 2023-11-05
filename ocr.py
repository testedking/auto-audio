import cv2
import pytesseract
import pyautogui
import numpy as np

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def capture_screen_and_ocr(x1, y1, x2, y2):
    # Capture a specific region of the screen using pyautogui
    screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))

    if screenshot is not None:
        # Convert the screenshot to a numpy array
        screenshot = np.array(screenshot)

        if screenshot is not None:
            # Convert the image to grayscale for OCR
            gray_image = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

            if gray_image is not None:
                # Use pytesseract to perform OCR
                recognized_text = pytesseract.image_to_string(gray_image)

                # Print the recognized text
                #print("Recognized Text:")
                #print(recognized_text)

                return recognized_text

    # Handle the case where processing fails
    return ""