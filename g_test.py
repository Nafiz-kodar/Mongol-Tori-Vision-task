import gi
import numpy as np
import cv2
from gi.repository import Gst, GstApp

gi.require_version("Gst", "1.0")
gi.require_version("GstApp", "1.0")
Gst.init(None)

pipeline=Gst.parse_launch("avfvideosrc ! videoconvert ! video/x-raw,format=BGR ! appsink name=sink")
appsink=pipeline.get_by_name("sink")
pipeline.set_state(Gst.State.PLAYING)

mode="n"
flip=False

try:
    while True:
        sample=appsink.try_pull_sample(Gst.SECOND)
        if sample is None:
            continue

        buffer=sample.get_buffer()
        caps=sample.get_caps()
        structure=caps.get_structure(0)
        width=structure.get_value("width")
        height=structure.get_value("height")

        success, map_info=buffer.map(Gst.MapFlags.READ)
        if not success:
            continue

        frame=np.frombuffer(map_info.data, np.uint8).reshape((height, width, 3))
        buffer.unmap(map_info)

        if mode=="r":
            frame=np.rot90(frame)
        if flip:
            frame=cv2.flip(frame, 1) 
        elif mode=="c":
            gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame=cv2.Canny(gray, 75, 150)
        elif mode=="g":
            frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif mode=="h":
            frame=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        elif mode=="l":
            frame=cv2.cvtColor(frame, cv2.COLOR_BGR2Lab)


        cv2.imshow("Processed Frame", frame)

        key=cv2.waitKey(1) & 0xFF
        if key==ord("q"):
            break
        elif key==ord("r"):
            mode="r"
        elif key==ord("c"):
            mode="c"
        elif key==ord("g"):
            mode="g"
        elif key==ord("h"):
            mode="h"
        elif key==ord("l"):
            mode="l"
        elif key==ord("n"):
            mode="n"
        elif key==ord("f"):
            flip=not flip  

except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
cv2.destroyAllWindows()
