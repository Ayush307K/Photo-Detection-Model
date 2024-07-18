
# Brand Logo Detection Pipeline

This project provides a comprehensive pipeline for detecting brand logos such as Pepsi and Coca-Cola in a video file and recording their presence with timestamps. It consists of two main files:

- `timestamp.py`: A Python script to detect logos in a video and record their timestamps.
- `video.ipynb`: A Jupyter Notebook providing a training file for the custom model.

## Table of Contents
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
  - [Running the Python Script](#running-the-python-script)
  - [Using the Jupyter Notebook](#using-the-jupyter-notebook)
- [Output](#output)

## Requirements
- Python 3.7+
- OpenCV
- Ultralytics YOLO
- Jupyter Notebook (for `video.ipynb`)
- Roboflow

## Setup
1. Clone the repository or download the project files.
2. Install the required Python libraries:
   ```sh
   pip install opencv-python ultralytics jupyter roboflow
   ```
3. Ensure you have the trained YOLO model file (`best.pt`) by running the training in `video.ipynb` and place it in the appropriate directory.

## Usage

### Running the Python Script
The `timestamp.py` script processes a video file to detect objects and records their timestamps.

1. Open a terminal and navigate to the directory containing `timestamp.py`.
2. Run the script:
   ```sh
   python timestamp.py
   ```
3. The script will read the video file, perform logo detection, and save the timestamps of detected objects in a JSON file named `timestamps.json`.

### Using the Jupyter Notebook
The `video.ipynb` notebook provides an interactive interface for custom model training on Coke and Pepsi logos.

1. Open a terminal and navigate to the directory containing `video.ipynb`.
2. Start Jupyter Notebook:
   ```sh
   jupyter notebook
   ```

## Output
The `timestamp.py` script outputs a `timestamps.json` file containing the timestamps of detected objects in the following format:
```json
{
    "0": [
        0.2,
        0.3,
        0.4,
        0.5,
        0.6,
        0.7,
        0.8,
        0.9,
        1.0,
    ],
    "1": [
        0.2,
        0.3,
        0.4,
        0.5,
        0.6,
        0.7,
        0.8,
        0.9,
        1.0,
    ]
}
```
