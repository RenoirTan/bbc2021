from pathlib import Path
import pickle
import shutil
import cv2
import face_recognition as frec
import pyttsx3 as tts


SAVED_DIR = Path(__file__).parents[1].resolve() / "saved"


def add_image(image, name: str) -> Path:
    pass
