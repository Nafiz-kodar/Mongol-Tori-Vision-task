

# GStreamer + OpenCV Live Camera Processing

This Python application uses **GStreamer** and **OpenCV** to capture live video from the default macOS camera (via `avfvideosrc`), process it in real time with several visual effects, and display the modified frames using OpenCV.

---

## 🔧 Features

- Real-time video feed from the macOS camera
- Keyboard-triggered video processing modes:
  - `n` – Normal (no effect)
  - `r` – Rotate 90° (clockwise)
  - `f` – Flip horizontally (toggle)
  - `g` – Grayscale
  - `c` – Canny edge detection
  - `h` – HSV color space
  - `l` – Lab color space
- Press `q` to quit the application

---

## 🛠 Requirements

- Python 3.7+
- GStreamer (with `gstreamer`, `gst-plugins-base`, `gst-plugins-good`, etc.)
- OpenCV (`opencv-python`)
- PyGObject (`PyGObject`, `python3-gi`)

### 📦 Install Dependencies

#### macOS (with Homebrew):
```bash
brew install gstreamer gst-plugins-base gst-plugins-good
pip install opencv-python PyGObject
```
### Run the Application
```bash
python video_processing.py
```

### How It Works
GStreamer Pipeline:

```bash
avfvideosrc ! videoconvert ! video/x-raw,format=BGR ! appsink
```

This fetches video from your macOS camera, converts it to BGR format, and sends it to an appsink for use in Python.

### Frame Processing:
Frames are read from the GStreamer buffer and mapped into a NumPy array. Based on keyboard input, the frames are processed and displayed using OpenCV.

### 💡 Tips
If no camera is detected, check macOS permissions:
System Preferences > Security & Privacy > Camera

You can modify the GStreamer pipeline to support USB webcams or IP cameras by replacing avfvideosrc.

