
import cv2
import numpy as np
from ultralytics import YOLO
import json

# Load the YOLOv8 model
model = YOLO('best.pt')

# Open the input video
input_video_path = 'testvideo.mp4'
cap = cv2.VideoCapture(input_video_path)

# Get the video's width, height, and FPS
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
output_video_path = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # codec
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Initialize a dictionary to store timestamps
timestamps = {0: [], 1: []}  # Change 0 and 1 to your specific class indices

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection
    results = model(frame)

    # Loop through the detected objects
    for obj in results[0].boxes:
        # Get bounding box coordinates
        x1, y1, x2, y2 = map(int, obj.xyxy[0])
        confidence = obj.conf[0]
        label = int(obj.cls[0])

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Put label and confidence
        text = f'{label} {confidence:.2f}'
        cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Save the timestamp if the object is of the specified class
        if label in timestamps:
            timestamp = round(frame_count / fps, 1)  # Convert frame count to timestamp and round to 1 decimal place
            if not timestamps[label] or timestamps[label][-1] != timestamp:
                timestamps[label].append(timestamp)

    # Write the frame to the output video
    out.write(frame)
    frame_count += 1

# Release the video capture and writer objects
cap.release()
out.release()

# Write timestamps to a JSON file
with open('timestamps.json', 'w') as f:
    json.dump(timestamps, f, indent=4)

print('Video processing complete.')
