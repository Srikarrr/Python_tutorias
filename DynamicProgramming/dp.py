import cv2
import torch
import numpy as np

class DynamicCV:
    def __init__(self, image_path=None, model=None, operations=None):
        self.image = None
        self.model = model
        self.operations = operations or []
        if image_path:
            self.load_image(image_path)

    # Dynamically add an operation to the pipeline
    def add_operation(self, operation):
        if callable(operation):
            self.operations.append(operation)

    # Dynamically remove an operation
    def remove_operation(self, operation):
        if operation in self.operations:
            self.operations.remove(operation)

    # Load image with OpenCV
    def load_image(self, path):
        self.image = cv2.imread(path)
        if self.image is None:
            raise ValueError("Image could not be loaded.")
        print(f"Image loaded: {path}")

    # Apply all operations to the image
    def process_image(self):
        for operation in self.operations:
            self.image = operation(self.image)
        return self.image

    # Run inference on the image if a model is defined
    def run_inference(self):
        if self.model is None:
            raise ValueError("No model provided.")
        
        # Assuming the model expects a tensor
        image_tensor = torch.tensor(self.image).float()
        image_tensor = image_tensor.unsqueeze(0)  # Add batch dimension

        with torch.no_grad():
            prediction = self.model(image_tensor)  # Model inference
        return prediction

# Example of dynamic image operations
def resize_image(image, size=(224, 224)):
    return cv2.resize(image, size)

def normalize_image(image):
    return image / 255.0

# Example of a simple CNN model (PyTorch)
class SimpleCNN(torch.nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = torch.nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.pool = torch.nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = torch.nn.Linear(32 * 112 * 112, 10)  # Example output size

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = x.view(x.size(0), -1)  # Flatten
        x = self.fc1(x)
        return x

# Usage Example:
# Initialize the dynamic class with a model and operations
cv = DynamicCV(image_path='path_to_image.jpg', model=SimpleCNN())

# Dynamically add operations
cv.add_operation(resize_image)
cv.add_operation(normalize_image)

# Process the image
processed_image = cv.process_image()

# Run inference if needed
prediction = cv.run_inference()
print("Model Prediction:", prediction)
