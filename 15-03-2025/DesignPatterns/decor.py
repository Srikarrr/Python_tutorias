class ImageProcessor:
    def process(self, image):
        raise NotImplementedError("Subclasses should implement this method!")

class EdgeDetectionProcessor(ImageProcessor):
    def process(self, image):
        return cv2.Canny(image, 100, 200)

class ImageProcessorDecorator(ImageProcessor):
    def __init__(self, processor: ImageProcessor):
        self._processor = processor

    def process(self, image):
        return self._processor.process(image)

class LoggingDecorator(ImageProcessorDecorator):
    def process(self, image):
        print("Processing image with edge detection...")
        return self._processor.process(image)

class ErrorHandlingDecorator(ImageProcessorDecorator):
    def process(self, image):
        try:
            return self._processor.process(image)
        except Exception as e:
            print(f"Error during processing: {e}")
            return None

# Client Code
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

processor = EdgeDetectionProcessor()
processor = LoggingDecorator(processor)  # Add logging
processor = ErrorHandlingDecorator(processor)  # Add error handling

processed_image = processor.process(image)
if processed_image is not None:
    cv2.imshow("Processed Image", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()