import pathlib
from typing import *
import cv2

IMAGES_PATH = pathlib.Path(__file__).parents[1].resolve() / "images"

def ex1():
    img = cv2.imread(str(IMAGES_PATH / "man-european-young.jpg"), -1)
    cv2.imshow("image", img)
    # Block until keypress
    cv2.waitKey() # 0 means forever
    cv2.destroyAllWindows()

def ex2():
    img = cv2.imread(str(IMAGES_PATH / "man-european-young.jpg"), -1)
    # dsize = (width, height)
    img = cv2.resize(img, (700, 300))
    img = cv2.flip(img, -1)
    img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
    # Params:
    # - Point 1
    # - Point 2
    # - BGR Value. Therefore (0, 0, 255) = #ff00000
    # - Thickness
    img = cv2.line(img, (0, 0), (200, 200), (0, 0, 255), 10)
    img = cv2.rectangle(img, (100, 100), (200, 200), (0, 0, 255), cv2.FILLED)
    img = cv2.putText(
        img,
        "penis",
        (50, 300),
        cv2.FONT_HERSHEY_COMPLEX,
        2,
        (0, 255, 255),
        3,
        cv2.LINE_AA # Line type
    )
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    while cv2.waitKey(0) != ord("a"): # Exit loop after 'a' pressed
        cv2.imshow("press `a` to exit", img)
    cv2.destroyAllWindows()
    cv2.imwrite(str(IMAGES_PATH / "man-european-young-edited.jpg"), img)


if __name__ == "__main__":
    ex2()
