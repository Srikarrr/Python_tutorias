#Example 4: List of Detected Features in Feature Matching
#In feature matching tasks (e.g., matching keypoints between two images),
#  you might work with a list of feature points (like SIFT or ORB keypoints).

import cv2
from typing import List

# Function that returns a list of keypoints for an image
def detect_keypoints(image: cv2.Mat) -> List[cv2.KeyPoint]:
    # Using ORB to detect keypoints
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(image, None)
    return keypoints

# Example usage
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
keypoints = detect_keypoints(image)

# Print the number of keypoints detected
print(f"Detected {len(keypoints)} keypoints.")

#In this example, List[cv2.KeyPoint] is used to represent a list of keypoints detected 
#using ORB (Oriented FAST and Rotated BRIEF) in the image.
