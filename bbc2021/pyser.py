from pathlib import Path
from typing import *
import cv2
import face_recognition as frec
import pickle

PICKLE_DIR = Path(__file__).parents[1].resolve() / "pickle"
IMAGES_PATH = Path(__file__).parents[1].resolve() / "images"
KNOWN_IMAGES = IMAGES_PATH / "known_faces_pic"
UNKNOWN_IMAGES = IMAGES_PATH / "unknown_pics"


def iter_known_images() -> Generator[Path, Path, None]:
    for person in KNOWN_IMAGES.iterdir():
        yield from person.iterdir()


def iter_unknown_images() -> Generator[Path, Path, None]:
    yield from UNKNOWN_IMAGES.iterdir()


def ex1():
    some_obj = [*range(1, 5), [*range(1, 4), "words"]]
    some_obj_path = PICKLE_DIR / "some_obj.pkl"
    with some_obj_path.open("wb") as f:
        pickle.dump(some_obj, f)


def ex2():
    deser_obj_path = PICKLE_DIR / "some_obj.pkl"
    with deser_obj_path.open("rb") as f:
        deser_obj = pickle.load(f)
        print(deser_obj)


def ex3():
    for image_path in iter_known_images():
        print(image_path.stem)
        image = frec.load_image_file(image_path)
        encoding = frec.face_encodings(image)[0]
        ser_obj_path = PICKLE_DIR / "images" / "{0}.pkl".format(
            image_path.stem
        )
        with ser_obj_path.open("wb") as f:
            pickle.dump((image, encoding), f)


def ex4():
    PICKLED_DIR = PICKLE_DIR / "images"
    for path in PICKLED_DIR.iterdir():
        with path.open("rb") as f:
            image, encoding = pickle.load(f)
            cv2.imshow(path.stem, image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


if __name__ == "__main__":
    ex4()
