import cv2

def process_frame(frame, mode):
    if mode=='g': 
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif mode=='c':  
        return cv2.Canny(frame, 100, 200)
    elif mode=='f':  
        return cv2.flip(frame, 1)
    elif mode=='n': 
        return frame
    else:
        return frame

def main():
    cap=cv2.VideoCapture(0)
    mode='n'  

    while True:
        ret, frame=cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        processed_frame=process_frame(frame, mode)
        cv2.imshow('Video Feed', processed_frame)

        key=cv2.waitKey(1) & 0xFF
        if key==ord('q'):  
            break
        elif key in [ord('g'), ord('c'), ord('f'), ord('r'), ord('n')]:
            mode=chr(key)

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()