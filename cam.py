import cv2
from IPython.display import display, clear_output
from PIL import Image
import numpy as np

# Open the default camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Could not open the camera.")

# Capture and display 10 frames as a demo
num_frames = 10

for i in range(num_frames):
    # Capture a frame
    ret, frame = cap.read()
    if not ret:
        print(f" Frame {i} failed to capture")
        break

    # Convert BGR to RGB (OpenCV -> PIL friendly)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img)

    # Display image in notebook
    display(img_pil)
    clear_output(wait=True)

# Release the camera when done
cap.release()

print("Finished capturing frames!")
