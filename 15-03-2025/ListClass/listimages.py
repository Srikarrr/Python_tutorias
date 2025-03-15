#Example 1: List of Images for Batch Processing

import cv2
from typing import List

# Load a list of images
def load_images(image_paths: List[str]) -> List[cv2.Mat]:
    images = []
    for path in image_paths:
        image = cv2.imread(path)
        if image is not None:
            images.append(image)
    return images

# Example usage
image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]
images = load_images(image_paths)
print(f"Loaded {len(images)} images.")

#Here, List[cv2.Mat] is used to indicate that the list
#contains OpenCV image matrices (cv2.Mat). This type hint is helpful 
# when you are processing multiple images simultaneously, such as for batch 
# processing in a deep learning model.

