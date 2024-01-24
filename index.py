import numpy as np
import cv2


def take_user_photo():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("לא ניתן לפתוח את המצלמה.")
        return
    ret, frame = cap.read()
    cv2.imshow("User Photo", frame)
    cap.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    take_user_photo()
