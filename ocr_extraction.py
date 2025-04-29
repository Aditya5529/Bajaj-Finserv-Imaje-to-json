import pytesseract
import cv2
from typing import List

def extract_text_from_image(image: cv2.Mat) -> List[str]:
    config = "--psm 6"
    text = pytesseract.image_to_string(image, config=config)
    
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines