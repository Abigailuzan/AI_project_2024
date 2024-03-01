from ultralytics import YOLO

# Load a pretrained model
model = YOLO('models/best.pt')

# Run Inference on the source
results = model(source='A_ripe_pineapple_sitting_on_a_wooden_table_with_a_.jpg', show=True, conf=0.35, save=True) # generator of Results objects
print(results)

# נכתוב פונקציה שתקבל שם של קובץ תמונה, תקרא את התמונה,
# ותיצור קובץ תווית (label) מתאים ל-YOLO.

import cv2
import os


def create_yolo_label(image_path, output_dir):
    # טעינת התמונה לקבלת המידות שלה
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"The image {image_path} could not be loaded.")

    # קבלת הגובה והרוחב של התמונה
    height, width, _ = image.shape

    # נניח שיש לנו כבר את הקורדינטות (x1, y1, x2, y2) של האובייקט בפורמט של פיקסלים
    # ונרצה להמיר אותם לפורמט של YOLO (cx, cy, w, h) כאשר הקורדינטות מנורמלות לטווח [0,1].
    # נשתמש בדוגמא קורדינטות נניח:
    x1, y1, x2, y2 = 100, 200, 400, 500  # דוגמא לקורדינטות

    # המרת הקורדינטות לפורמט YOLO
    cx = ((x1 + x2) / 2) / width
    cy = ((y1 + y2) / 2) / height
    w = (x2 - x1) / width
    h = (y2 - y1) / height

    # נניח שהקטגוריה (class) של האובייקט היא 2
    class_id = 2

    # כתיבת הקורדינטות לקובץ תווית
    label_name = os.path.splitext(os.path.basename(image_path))[0] + '.txt'
    label_path = os.path.join(output_dir, label_name)

    with open(label_path, 'w') as label_file:
        label_file.write(f"{class_id} {cx} {cy} {w} {h}\n")

    return label_path


# הפעלת הפונקציה על דוגמא של תמונה שהועלתה
image_path = 'A_realistic_photo_of_an_apple_inside_a_fruit_bowl,.jpg'
output_dir = 'after8_1.jpg'
label_file_path = create_yolo_label(image_path, output_dir)

#label_file_path
