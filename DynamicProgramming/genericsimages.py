from typing import TypeVar, Generic
import numpy as np
from PIL import Image

T = TypeVar('T')

class ImageTransformer(Generic[T]):
    def __init__(self, image: T):
        self.image = image

    def rotate(self, angle: float) -> T:
        """Rotate the image."""
        if isinstance(self.image, np.ndarray):
            # Rotate the numpy array image (OpenCV can be used)
            return np.rot90(self.image, k=int(angle / 90))  # Simple rotation logic
        elif isinstance(self.image, Image.Image):
            # Rotate the PIL Image
            return self.image.rotate(angle)  # Rotate using Pillow
        else:
            raise ValueError("Unsupported image type")

# Example usage with numpy array image
image_np = np.random.rand(100, 100, 3)  # A dummy numpy image
transformer_np = ImageTransformer(image_np)
rotated_image_np = transformer_np.rotate(90)

# Example usage with a PIL image
image_pil = Image.open("example.jpg")  # Replace with an actual file path
transformer_pil = ImageTransformer(image_pil)
rotated_image_pil = transformer_pil.rotate(90)
