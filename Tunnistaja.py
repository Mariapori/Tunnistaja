
import cv2
from mtcnn import MTCNN
import imutils

tunnistaja = MTCNN()
video_lahde = cv2.VideoCapture("rtsp://10.0.0.140")
video_lahde.set(cv2.CAP_PROP_BUFFERSIZE,1)

while(True):
    video_lahde.set(cv2.CAP_PROP_POS_FRAMES,0)
    ret, frame = video_lahde.read()
    if ret == False:
        print("Ei ole")
        break
    else:
        frame = imutils.resize(frame,width=1280,height=640)
        result = tunnistaja.detect_faces(frame)
        print(result)

        if len(result) > 0:
            tunnistusIkkuna = result[0]['box']

            cv2.rectangle(frame,(tunnistusIkkuna[0],tunnistusIkkuna[1]),(tunnistusIkkuna[0]+tunnistusIkkuna[2],tunnistusIkkuna[1]+tunnistusIkkuna[3]),(0,255,0),2)

        cv2.imshow("Mariaporin valvontakamera",frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break

video_lahde.release()
cv2.destroyAllWindows()