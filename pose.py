"""  import cv2
from ultralytics import YOLO
model=YOLO("yolo11n-pose.pt")
print("Model loaded successfully!")

vidcap = cv2.VideoCapture("16538871-uhd_2160_3840_24fps.mp4")
while True:
   success, frame = vidcap.read()
   if not success:
       break
   # Resize frame to 700x500 pixels
   resized_frame = cv2.resize(frame, (700, 500))
   # Display resized frame
   cv2.imshow("Resized Frame", resized_frame)

   if cv2.waitKey(10) & 0xFF == 27: # ESC to exit
       break
vidcap.release()
results=model.predict(
    source=r"16538871-uhd_2160_3840_24fps.mp4",
    imgsz=640,
    save=True,
    show=True,
    project="Posing",
    name="Output", 
)
print("Posing! Completed")
print(results[0].boxes)
print(results[0].keypoints)
cv2.destroyAllWindows()
import cv2

cap = cv2.VideoCapture("16538871-uhd_2160_3840_24fps.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("resized_video.mp4", fourcc, 24, (700, 500))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resized = cv2.resize(frame, (700, 500))
    out.write(resized)


print("Resized video saved successfully!")

from ultralytics import YOLO
model=YOLO("yolo11n-pose.pt")
print("Model loaded successfully!")

vidcap = cv2.VideoCapture("16538871-uhd_2160_3840_24fps.mp4")
while True:
   success, frame = vidcap.read()
   if not success:
       break
   # Resize frame to 700x500 pixels
   resized_frame = cv2.resize(frame, (700, 500))
   # Display resized frame
   cv2.imshow("Resized Frame", resized_frame)

   if cv2.waitKey(10) & 0xFF == 27: # ESC to exit
       break
vidcap.release()
results=model.predict(
    source=r"resized_video.mp4",
    imgsz=640,
    save=True,
    show=True,
    project="Posing",
    name="Output", 
)
print("Posing! Completed")
print(results[0].boxes)
print(results[0].keypoints)
 
cap.release()
out.release()
cv2.destroyAllWindows() """
import cv2
from ultralytics import YOLO

# Read original video
cap = cv2.VideoCapture("16538871-uhd_2160_3840_24fps.mp4")

# Check if video opened
if not cap.isOpened():
    print("Error: Cannot open input video")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("resized_video.mp4", fourcc, fps, (700, 500))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    resized = cv2.resize(frame, (700, 500))
    out.write(resized)

# IMPORTANT: Close the files BEFORE using YOLO
cap.release()
out.release()

print("Resized video saved successfully!")

# Load pose model
model = YOLO("yolo11n-pose.pt")

# Run pose detection
results = model.predict(
    source="resized_video.mp4",
    save=True,
    show=True,
    project="Posing",
    name="Output"
)

print("Pose Detection Completed!")
cv2.destroyAllWindows()