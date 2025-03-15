from typing import TypeVar, Generic
import numpy as np
from PIL import Image

# Define a generic type that will be used in our class
T = TypeVar('T')

class ImageProcessor(Generic[T]):
    def __init__(self, image: T):
        self.image = image

    def apply_filter(self) -> T:
        """Applies a simple image filter (blur for example)."""
        if isinstance(self.image, np.ndarray):
            # Using OpenCV or other libraries to apply a filter to the numpy image
            return np.zeros_like(self.image)  # Example: simply returns a zero array
        elif isinstance(self.image, Image.Image):
            # Using Pillow to apply a filter to a PIL Image
            return self.image.filter(ImageFilter.BLUR)  # Apply blur to PIL image
        else:
            raise ValueError("Unsupported image type")
        
    def show_image(self) -> None:
        """Displays the image."""
        if isinstance(self.image, np.ndarray):
            import matplotlib.pyplot as plt
            plt.imshow(self.image)
            plt.show()
        elif isinstance(self.image, Image.Image):
            self.image.show()

# Example usage with numpy array image (e.g., an OpenCV image)
image_np = np.random.rand(100, 100, 3)  # A dummy numpy image
processor_np = ImageProcessor(image_np)
processed_image_np = processor_np.apply_filter()
processor_np.show_image()

# Example usage with a PIL image
image_pil = Image.open("example.jpg")  # Replace with an actual file path
processor_pil = ImageProcessor(image_pil)
processed_image_pil = processor_pil.apply_filter()
processor_pil.show_image()
