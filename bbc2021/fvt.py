import face_recognition as frec
from pathlib import Path
import cv2
import pickle
from PIL import Image
import shutil
import PySimpleGUI as psgui
import pyttsx3 as tts
import random
import datetime
from threading import Thread


engine = tts.init()


def say(text):
    engine.say(text)
    engine.runAndWait()


ROOT_DIR = Path(__file__).parents[1].resolve()
PICKLED_DIR = ROOT_DIR / "pickle" / "images"


def get_known():
    known = []
    for path in PICKLED_DIR.iterdir():
        with path.open("rb") as f:
            known.append(pickle.load(f))
    return known


def ex1():
    TOLERANCE: int = 0.5
    COLOR = (0, 0, 255)
    THICKNESS = 5
    known = get_known()
    known_encodings = [k[1] for k in known]
    video = cv2.VideoCapture(0)
    while True:
        ret, image = video.read()
        locations = frec.face_locations(image)
        encodings = frec.face_encodings(image, locations)
        for location, encoding in zip(locations, encodings):
            results = list(frec.face_distance(known_encodings, encoding))
            closest = min(results)
            if closest <= TOLERANCE:
                name = "Ayy"
            else:
                name = "Unknown"
            top, right, bottom, left = location
            cv2.rectangle(
                image, (left, top), (right, bottom), COLOR, THICKNESS
            )
            cv2.rectangle(
                image, (left, bottom), (right, bottom+22), COLOR, cv2.FILLED
            )
            cv2.putText(
                image,
                name,
                (left+10, bottom+10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (200, 200, 200),
                2
            )
        cv2.imshow("video", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    ex1()
