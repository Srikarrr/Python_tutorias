import threading
import cv2
import time

# Function to capture frames from the webcam
def capture_frames(frame_queue):
    cap = cv2.VideoCapture(0)  # Open webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_queue.append(frame)  # Store captured frame
    cap.release()

# Function to process the frames (e.g., convert to grayscale)
def process_frames(frame_queue):
    while True:
        if frame_queue:
            frame = frame_queue.pop(0)  # Get the next frame from the queue
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Processed Frame', gray_frame)  # Show the processed frame
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# Queue to store frames
frame_queue = []

# Create threads
capture_thread = threading.Thread(target=capture_frames, args=(frame_queue,))
process_thread = threading.Thread(target=process_frames, args=(frame_queue,))

# Start threads
capture_thread.start()
process_thread.start()

# Wait for threads to complete
capture_thread.join()
process_thread.join()

cv2.destroyAllWindows()


#Explanation:
#Capture Thread: Continuously captures frames from the webcam and adds them to a shared queue.
#Processing Thread: Continuously checks the queue for new frames and processes them (in this case, converting them to grayscale).
#Both threads run concurrently, allowing the system to capture and process frames in parallel, leading to faster video processing.