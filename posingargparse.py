import cv2
from ultralytics import YOLO

# Load pose model

# Run pose detection
def run_pose(model_path,source,save_dir,conf,save_name="Output"):
  model = YOLO(model_path)
  result= model.predict(
    conf=conf,
    source=source,
    save=True,
    show=True,
    project=save_dir,
    name=save_name,
)
  print("Pose Detection Completed!")
  print("Classes",model.names)
  print(result[0].keypoints)
  print("No of Classes",len(model.names))
  print("Posing Completed",result[0].keypoints)
  cv2.imshow("Posing Completed",result[0].plot)
  cv2.imwrite("output.jpg",result[0].plot)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

  return result









