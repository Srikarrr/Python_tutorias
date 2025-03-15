from typing import TypeVar
from PIL import Image
import numpy as np

T = TypeVar('T')

def resize_image(image: T, width: int, height: int) -> T:
    """Resizes an image (numpy.ndarray or PIL.Image)."""
    if isinstance(image, np.ndarray):
        return np.resize(image, (height, width, image.shape[2]))  # Resize numpy image
    elif isinstance(image, Image.Image):
        return image.resize((width, height))  # Resize PIL Image
    else:
        raise ValueError("Unsupported image type")

# Example usage with numpy image
image_np = np.random.rand(100, 100, 3)  # A dummy numpy image
resized_image_np = resize_image(image_np, 50, 50)

# Example usage with a PIL image
image_pil = Image.open("example.jpg")  # Replace with an actual file path
resized_image_pil = resize_image(image_pil, 50, 50)
