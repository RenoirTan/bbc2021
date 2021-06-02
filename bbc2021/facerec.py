import pathlib
from typing import *
import cv2
import face_recognition
import numpy as np


IMAGES_PATH = pathlib.Path(__file__).parents[1].resolve() / "images"
KNOWN_IMAGES = IMAGES_PATH / "known_faces_pic"
UNKNOWN_IMAGES = IMAGES_PATH / "unknown_pics"


def iter_known_images() -> Generator[pathlib.Path, pathlib.Path, None]:
    for person in KNOWN_IMAGES.iterdir():
        yield from person.iterdir()


def iter_unknown_images() -> Generator[pathlib.Path, pathlib.Path, None]:
    yield from UNKNOWN_IMAGES.iterdir()


# video = cv2.VideoCapture(0)
# if cv2.waitKey(1) & 0xFF == ord("q") # Resolve to ASCII 1-byte
#     cv2.destroyAllWindows()


def ex1():
    known_encodings = []
    known_names = []
    for known_path in iter_known_images():
        print("Registering {0}".format(known_path))
        known = face_recognition.load_image_file(known_path)
        known_encoding = face_recognition.face_encodings(known)[0]
        known_encodings.append(known_encoding)
        known_names.append(known_path)
    for unknown_path in iter_unknown_images():
        print("Examining {0}".format(unknown_path))
        unknown = face_recognition.load_image_file(
            unknown_path
        )
        unknown_facelocs = face_recognition.face_locations(unknown)
        unknown_encodings = face_recognition.face_encodings(
            unknown, unknown_facelocs
        )
        tolerance = 0.5 # 1 means the same face
        for location, encoding in zip(unknown_facelocs, unknown_encodings):
            # results is a numpy array
            results = face_recognition.face_distance(known_encodings, encoding)
            print(results)
            closest = min(results)
            name = "Unknown"
            if closest <= tolerance:
                print("Match found!")
                print("Closeness: {0}".format(closest))
                # Get minimum index
                index = np.where(results == np.amin(results))[0][0]
                print(index)
                name = str(known_names[index].name)
            else:
                print("No match found...")
            top, right, bottom, left = location
            # Draw frame around person's face
            unknown = cv2.rectangle(
                unknown,
                (left, top),
                (right, bottom),
                (0, 0, 255),
                5
            )
            unknown = cv2.rectangle(
                unknown,
                (left, bottom),
                (right, bottom+60), # 22 pixels thick
                (0, 0, 255),
                -1 # Fill bottom rectangle
            )
            unknown = cv2.putText(
                unknown,
                name,
                (left+10, bottom+30),
                cv2.FONT_HERSHEY_SIMPLEX,
                2,
                (0, 0, 0),
                3
            )
            height = unknown.shape[0]
            width = unknown.shape[1]
            ratio = width / height
            new_height = 500
            new_width = int(new_height * ratio)
            unknown = cv2.resize(unknown, (new_width, new_height))
            cv2.imshow("Person", unknown)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


if __name__ == "__main__":
    ex1()
