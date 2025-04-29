import cv2
import numpy as np
from PIL import Image
import io

def preprocess_image(file_bytes: bytes) -> np.ndarray:

    image = Image.open(io.BytesIO(file_bytes)).convert('RGB')
    image = np.array(image)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    thresh = cv2.adaptiveThreshold(
        blurred, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 
        11, 2
    )
    return thresh