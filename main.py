import cv2
import tkinter as tk
from PIL import Image, ImageTk
from fer import FER
import face_recognition
import os
import logging

class EmotionRecognitionDemo:
    def __init__(self, window, window_title):
        # create a window and a webcam feed
        self.window = window
        self.window.title(window_title)

        # webcam is usually 0
        self.cap = cv2.VideoCapture(0)

        self.canvas = tk.Canvas(window, width=self.cap.get(3), height=self.cap.get(4))
        self.canvas.pack()

        # create labels
        self.emotion_label = tk.Label(window, text="Detected Emotion: None", font=("Helvetica", 16))
        self.name_label = tk.Label(window, text="Recognized Face: ", font=("Helvetica", 16))
        self.name_label.pack(pady=10)
        self.emotion_label.pack(pady=10)

        # name entry field
        self.name_entry = tk.Entry(window)
        self.name_entry.pack(pady=10)

        # add buttons
        self.train_button = tk.Button(window, text="Train Face", command=self.train_face)
        self.train_button.pack(pady=10)

        self.recognize_button = tk.Button(window, text="Recognize Face", command=self.recognize_face)
        self.recognize_button.pack(pady=10)

        # create fer instance
        self.fer = FER()

        self.known_faces = []
        self.face_encodings = []
        self.face_names = []
        self.training_mode = False

        self.update()

    def update(self):
        # grab a single frame
        ret, frame = self.cap.read()

        if ret:
            # detect emotions on the face
            emotions = self.fer.detect_emotions(frame)

            if emotions:
                # get highest correlation emotion
                dominant_emotion = max(emotions[0]["emotions"].items(), key=lambda x: x[1])[0]

                # update emotion label in the gui
                self.emotion_label.config(text=f"Detected Emotion: {dominant_emotion}")

                # have to convert the image to a pil image to display it :(
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(img)
                img = ImageTk.PhotoImage(image=img)

                # update image
                self.canvas.img = img
                self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # grab next image after 10 ms
        self.window.after(10, self.update)

    def train_face(self):
        # switch to train mode
        self.training_mode = True

        # grab a single frame
        ret, frame = self.cap.read()

        if ret:
            # find all faces and encoding in the frame
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            # if one of the faces is detected...
            # TODO: check if the detected face isnt in the dataset!
            if face_encodings:
                # assuming theres only one face in frame.
                face_encoding = face_encodings[0]

                name = self.name_entry.get()

                # add face and name to the lists.
                self.face_encodings.append(face_encoding)
                self.face_names.append(name)

        self.training_mode = False

    def recognize_face(self):
        # recognizing face isnt a training mode
        self.training_mode = False

        # grab a frame.
        ret, frame = self.cap.read()

        if ret:
            # grab all faces and encodings
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            # check face against all faces we know.
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(self.face_encodings, face_encoding)
                name = "Unknown"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = self.face_names[first_match_index]
                    self.name_label.config(text=f"Detected Face: {name}")

                print(f"Recognized face: {name}")

    def close_app(self):
        # close
        self.cap.release()
        self.window.destroy()


# create tkinter and run the app
root = tk.Tk()
app = EmotionRecognitionDemo(root, "Project Awesome")
log_file_path = os.path.join(os.getcwd(), 'event.log')
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename=log_file_path, level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='[%d %b %Y %H:%M:%S]')
logging.info('[SYS_START] [1] [...] [SU] [...] [...]')
print("Log file path:", log_file_path)
root.mainloop()
