
# Face Detection with OpenCV

This project uses OpenCV's Haar Cascade classifier to detect faces in either a static image or a live video feed from the webcam. You can specify whether to perform face detection on an image or a live video stream using command-line arguments.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Command-line Arguments](#command-line-arguments)
- [Examples](#examples)
- [License](#license)

## Features
- Detects faces in an image or live video feed.
- Draws bounding boxes around detected faces.
- Easily switch between image and video modes with command-line arguments.

## Requirements
- Python 3.10 and above
- OpenCV library

## Installation
1. **Clone this repository:**
   ```bash
   git clone https://github.com/GLITCH-08/CV_P.git
   cd CV_P
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/Scripts/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install opencv-python
   ```

4. **Download the Haar Cascade file:**
   Make sure to place the `haarcascade_frontalface_default.xml` file in the same directory as the code, or update the path in the script.

   - You can download the Haar Cascade XML file from [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

## Usage

### Running the code:

#### For Image Mode:
To detect faces in an image, provide the path to the image file as the second argument:
```bash
python main.py img path/to/image.jpg
```

#### For Video Mode:
To detect faces in a live video feed, run the script with the `vid` argument:
```bash
python main.py vid
```

### Command-line Arguments:
- `img`: Perform face detection on an image file. You must provide the path to the image as a second argument.
- `vid`: Perform face detection on a live video feed from the webcam.

### Example Commands:

#### Image Detection Example:
```bash
python main.py img path/to/image.jpg
```

#### Video Detection Example:
```bash
python main.py vid
```

### Closing the video feed:
Press `q` to quit the live video feed when running in video mode.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
