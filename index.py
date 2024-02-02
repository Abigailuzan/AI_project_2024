import numpy as np
import cv2
import tensorflow as tf
import cv2
import tkinter as tk
from tkinter import filedialog


# Function to take a photo
def take_or_upload_photo():
    # Ask the user to take a new photo or upload one
    choice = input("Type 'C' to capture a photo or 'U' to upload a photo: ").strip().upper()

    if choice == 'C':
        # Initialize the camera
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera.")
            return False

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            cv2.imshow('Press SPACE to take photo', frame)
            if cv2.waitKey(1) == 32:
                cv2.imwrite('user_photo.jpg', frame)
                print("Photo captured and saved.")
                break

        cap.release()
        cv2.destroyAllWindows()
        return 'user_photo.jpg'

    elif choice == 'U':
        # Initialize Tkinter root
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        file_path = filedialog.askopenfilename()  # Open the file dialog
        if file_path:
            print(f"Photo uploaded: {file_path}")
            return file_path
        else:
            print("No photo uploaded.")
            return False

    else:
        print("Invalid choice.")
        return False


def take_user_photo():
    # Example usage
    photo_path = take_or_upload_photo()
    if photo_path:
        # Process the photo using its path
        print(f"Photo path: {photo_path}")


# Function to run object detection on a photo
def detect_objects(image_path, model):
    # Load image
    image = cv2.imread(image_path)
    # Convert image to tensor
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis, ...]
    # Run detection
    model_fn = model.signatures['serving_default']
    output_dict = model_fn(input_tensor)
    # Extract boxes, classes, and scores
    boxes = output_dict['detection_boxes'][0].numpy()
    classes = output_dict['detection_classes'][0].numpy().astype(np.int64)
    scores = output_dict['detection_scores'][0].numpy()
    # Display results
    for i in range(len(scores)):
        if scores[i] > 0.5:
            print(f'Object {i}: Class {classes[i]}, Score: {scores[i]}')


# Main function
if __name__ == "__main__":
    if take_user_photo():
        # Load a pre-trained model (you need to download and specify the correct path)
        model = tf.saved_model.load('food-101')
        # Run object detection on the captured photo
        detect_objects('user_photo.jpg', model)
