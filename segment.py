import cv2
from ultralytics import YOLO

# Read original video
cap = cv2.VideoCapture("14919185-uhd_2160_3840_60fps.mp4")

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
model = YOLO("yolo11n-seg.pt")

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