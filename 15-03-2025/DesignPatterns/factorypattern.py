import cv2
import numpy as np

# Abstract Base Class for Image Processors
class ImageProcessor:
    def process(self, image):
        raise NotImplementedError("Subclasses should implement this method!")

# Concrete Classes for Different Image Processors
class EdgeDetectionProcessor(ImageProcessor):
    def process(self, image):
        # Applying Canny Edge Detection
        return cv2.Canny(image, 100, 200)

class BlurProcessor(ImageProcessor):
    def process(self, image):
        # Applying Gaussian Blur
        return cv2.GaussianBlur(image, (15, 15), 0)

class SharpenProcessor(ImageProcessor):
    def process(self, image):
        # Applying Sharpening Filter
        kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
        return cv2.filter2D(image, -1, kernel)

# Factory Class to Create the Image Processor
class ImageProcessorFactory:
    @staticmethod
    def create_processor(processor_type):
        if processor_type == "edge_detection":
            return EdgeDetectionProcessor()
        elif processor_type == "blur":
            return BlurProcessor()
        elif processor_type == "sharpen":
            return SharpenProcessor()
        else:
            raise ValueError("Unknown processor type!")

# Client Code to Use the Factory
def main():
    # Load an image
    image = cv2.imread('sample_image.jpg', cv2.IMREAD_GRAYSCALE)

    # Create the appropriate image processor using the Factory
    processor_type = "edge_detection"  # This can be dynamically set based on user input or config
    processor = ImageProcessorFactory.create_processor(processor_type)

    # Process the image
    processed_image = processor.process(image)

    # Display the processed image
    cv2.imshow(f"Processed Image - {processor_type}", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()