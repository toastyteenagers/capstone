import torch.cuda
from facial_emotion_recognition import EmotionRecognition
import face_recognition as fr
import cv2 as cv
print(torch.cuda.is_available())
er: EmotionRecognition = EmotionRecognition(device='gpu', gpu_id=0)

cam = cv.VideoCapture(0)

success, frame = cam.read()

frame = er.recognise_emotion(frame, return_type='BGR')

cv.imshow("frame", frame)

while True:
    key = cv.waitKey(10)
    if key & 0xff == 27:
        break
def main():
    pass

if __name__ == '__main__':
    main()
