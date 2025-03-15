import cv2

class CameraCapture:
    # A static variable to hold the single instance of the class
    _instance = None

    # Private constructor to prevent creating a new instance from outside
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating CameraCapture instance.")
            cls._instance = super(CameraCapture, cls).__new__(cls)
            cls._instance._initialize_camera()
        return cls._instance
    
    def _initialize_camera(self):
        # Initialize the camera (in this case, using OpenCV)
        self.camera = cv2.VideoCapture(0)  # Open default camera
        if not self.camera.isOpened():
            raise Exception("Could not open video device")
    
    def capture_frame(self):
        # Capture a frame from the camera
        ret, frame = self.camera.read()
        if not ret:
            print("Failed to capture frame.")
            return None
        return frame
    
    def release_camera(self):
        # Release the camera when done
        self.camera.release()
        print("Camera released.")

# Client code that uses the CameraCapture Singleton
def main():
    # Get the singleton instance
    camera1 = CameraCapture()
    
    # Capture a frame
    frame1 = camera1.capture_frame()
    if frame1 is not None:
        cv2.imshow("Captured Frame", frame1)
        cv2.waitKey(0)
    
    # Get another reference to the CameraCapture instance
    camera2 = CameraCapture()
    
    # Check if both references point to the same object
    print(f"Camera1 and Camera2 are the same object: {camera1 is camera2}")

    # Release the camera
    camera1.release_camera()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()