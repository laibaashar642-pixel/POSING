# YOLO11 Human Pose Estimation

This repository implements real-time human pose estimation using the Ultralytics YOLO11 Pose model. The project detects human body keypoints from images, videos, and webcam streams, making it suitable for applications such as activity recognition, motion analysis, fitness monitoring, and computer vision research.

## Overview

The project provides a command-line interface for running human pose estimation using a pretrained YOLO11 Pose model. It supports multiple input sources and automatically saves annotated outputs with detected keypoints and skeleton connections.

## Features

- Real-time human pose estimation
- Supports images, videos, and webcam input
- Uses pretrained YOLO11 Pose model
- Configurable confidence threshold
- Automatic saving of annotated results
- Command-line interface using `argparse`

---

## Project Structure

```
Posing/
│── main.py                   # Main entry point
│── posingargparse.py         # Pose estimation pipeline
│── requirements.txt          # Project dependencies
│── README.md                 # Project documentation
│
├── Sample_Test/              # Sample input images/videos
├── Person Detection/         # Output directory
└── output.jpg                # Sample output image
```

---

## Requirements

- Python 3.10 or later
- OpenCV
- Ultralytics YOLO

Install the required packages using:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install ultralytics opencv-python
```

---

## Usage

Run pose estimation using the following command:

```bash
python main.py --task pose --model yolo11n-pose.pt --source Sample_Test/sample.mp4 --project "Person Detection"
```

### Command-Line Arguments

| Argument | Description |
|----------|-------------|
| `--task` | Task to perform (`pose`) |
| `--model` | Path to the YOLO11 Pose model |
| `--source` | Image, video, or webcam source |
| `--conf` | Confidence threshold (default: 0.5) |
| `--project` | Directory to save output |

Example:

```bash
python main.py ^
--task pose ^
--model yolo11n-pose.pt ^
--source Sample_Test/sample.mp4 ^
--project "Person Detection"
```

---

## Output

The generated output includes:

- Human body keypoints
- Skeleton connections
- Annotated images or videos
- Confidence-based pose predictions

All output files are saved in the specified project directory.

---

## Model

This project uses the pretrained **YOLO11 Pose (`yolo11n-pose.pt`)** model provided by Ultralytics.

---

## Resources

The following Google Drive contains:

- Pretrained model weights
- Sample test images and videos
- Pose estimation results

Google Drive:

https://drive.google.com/drive/folders/1AjQNUrTq1IlriMJ2dgWtuUI5dlO_zoaf?usp=drive_link

---

## Technologies Used

- Python
- OpenCV
- Ultralytics YOLO11
- argparse

---

## Author

**Laiba Ashar**

BS Information Technology

Python & Computer Vision Developer

---

## License

This project is intended for educational and research purposes.
