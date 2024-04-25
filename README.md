## Object Detection with OpenCV

This repository contains code for detecting objects in a specific color range using OpenCV, a popular computer vision library in Python. The code captures video from a camera feed and identifies objects in the specified color range, drawing bounding boxes around them.

### Code Overview:

#### `main.py`:

- This script captures video from a camera feed and performs object detection based on color.
- It uses OpenCV to process video frames and detect objects in a specific color range.
- Bounding boxes are drawn around detected objects, indicating their location within the frame.

#### `util.py`:

- This module contains a utility function `get_limits` used for defining the lower and upper limits of the HSV color range for object detection.
- The `get_limits` function takes a color in the BGR (Blue-Green-Red) color space and converts it to the corresponding range in the HSV (Hue-Saturation-Value) color space.

### Usage:

1. Make sure you have Python and OpenCV installed on your system.
2. Clone this repository to your local machine.
3. Adjust the color range in `main.py` to match the color of the objects you want to detect.
4. Run `main.py`.
5. Press 'q' to exit the application.

### Dependencies:

- Python 3.x
- OpenCV (`opencv-python` package)
- NumPy (`numpy` package)
- Pillow (`Pillow` package)

### Contributions:

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
