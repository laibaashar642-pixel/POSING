# Image and Video Segmentation using YOLO11 Segmentation

## Overview

This project performs object segmentation using the pretrained YOLO11 Segmentation model. Unlike object detection, segmentation predicts pixel-level masks for every detected object.

## Features

* Instance segmentation
* Pixel-wise object masks
* Video segmentation
* Webcam segmentation
* Save segmented output
* Fast inference

## Technologies Used

* Python 3.13
* OpenCV
* Ultralytics YOLO11
* PyTorch

## Pretrained Model

```
yolo11n-seg.pt
```

## Project Structure

```
Segmentation/
│── segmentation.py
│── README.md
│── requirements.txt
│── .gitignore
│── input_video.mp4
└── Output/
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python segmentation.py
```

## Output

* Segmentation masks
* Object detection
* Saved segmented video
* Pixel-level predictions

## Author

@Laiba Ashar
BS Information Technology
