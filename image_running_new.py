import cv2

from ultralytics import YOLO
# הנתיב לתמונה שעליה לבצע את הזיהוי
image_path = 'A_realistic_photo_of_a_hamburger_with_a_side_of_fr.jpg'
# הנתיב לשמירת התמונה המעובדת
image_path_out = 'after13_1.jpg'

# טעינת התמונה
image = cv2.imread(image_path)

# הנתיב לקובץ המודל של YOLO
model_path = 'best.pt'
# טעינת המודל
model = YOLO(model_path)  # טעינת מודל מותאם אישית

# הגדרת סף לזיהוי
threshold = 0.1

# זיהוי אובייקטים בתמונה
resultss = model(image)


for results in resultss:
# ציור מלבן סביב כל אובייקט שזוהה וכתיבת שם האובייקט
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(image, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

# שמירת התמונה המעובדת
cv2.imwrite(image_path_out, image)


