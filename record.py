import cv2
from datetime import datetime

def record():
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(f'recordings/{datetime.now().strftime("%H-%M-%S")}.avi', fourcc, 10.0, (640, 480), isColor=True)

    out.set(cv2.CAP_PROP_BITRATE, 500000) # set bitrate to 500000

    while True:
        _, frame = cap.read()

        cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50,50), cv2.FONT_HERSHEY_COMPLEX,
                        0.6, (255,255,255), 2)

        out.write(frame)

        cv2.imshow("esc. to stop", frame)

        if cv2.waitKey(1) == 27:
            cap.release()
            out.release() # release the video writer
            cv2.destroyAllWindows()
            break 

