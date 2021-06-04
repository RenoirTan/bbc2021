from time import sleep
import cv2
import numpy as np
import pyautogui as gui
import tensorflow as tf
import tensorflow.keras as tf_keras

def ex1():
    while cv2.waitKey(0) & 0xFF == ord("q"):
        pass
    cv2.destroyAllWindows()


if __name__ == "__main__":
    ex1()