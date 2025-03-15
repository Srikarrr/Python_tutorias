class ImageTransformationStrategy:
    def transform(self, image):
        raise NotImplementedError("Subclasses should implement this method!")

class ResizeStrategy(ImageTransformationStrategy):
    def transform(self, image):
        return cv2.resize(image, (100, 100))

class RotateStrategy(ImageTransformationStrategy):
    def transform(self, image):
        return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

class CropStrategy(ImageTransformationStrategy):
    def transform(self, image):
        return image[50:200, 50:200]  # Cropping a region of interest

class ImageTransformer:
    def __init__(self, strategy: ImageTransformationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ImageTransformationStrategy):
        self._strategy = strategy

    def apply_transformation(self, image):
        return self._strategy.transform(image)

# Client Code
image = cv2.imread('image.jpg')

transformer = ImageTransformer(ResizeStrategy())  # Using Resize strategy
transformed_image = transformer.apply_transformation(image)
cv2.imshow("Resized Image", transformed_image)
cv2.waitKey(0)

# Changing strategy to rotation
transformer.set_strategy(RotateStrategy())
transformed_image = transformer.apply_transformation(image)
cv2.imshow("Rotated Image", transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
