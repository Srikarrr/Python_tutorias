class Observer:
    def update(self, data):
        raise NotImplementedError("Subclasses should implement this method!")

class ImageDisplay(Observer):
    def update(self, image):
        print("Displaying the processed image")
        cv2.imshow("Processed Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

class ImageLogger(Observer):
    def update(self, image):
        print("Logging the image process")

class ImageProcessorSubject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, image):
        for observer in self._observers:
            observer.update(image)

    def process_image(self, image):
        processed_image = cv2.GaussianBlur(image, (15, 15), 0)
        self.notify(processed_image)

# Client Code
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Create Subject (image processor) and Observers
processor = ImageProcessorSubject()
display = ImageDisplay()
logger = ImageLogger()

# Attach observers
processor.attach(display)
processor.attach(logger)

# Process the image and notify observers
processor.process_image(image)
