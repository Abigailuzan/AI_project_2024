import cv2

from ultralytics import YOLO
# הנתיב לתמונה שעליה לבצע את הזיהוי
image_path = r'pic\friedchicken-rice.jpg'  # Change this to the path of your image
image_path_out = '{}_out.jpg'.format(image_path)

# טעינת התמונה
image = cv2.imread(image_path)
# Resize the image to 640x640 pixels
image_resized = cv2.resize(image, (640, 640))
# הנתיב לקובץ המודל של YOLO
model_path ='bestFoodTaste.pt'
# טעינת המודל
model = YOLO(model_path)  # טעינת מודל מותאם אישית

# הגדרת סף לזיהוי
threshold = 0.1

# זיהוי אובייקטים בתמונה
resultss = model(image_resized)


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
# import cv2
# from ultralytics import YOLO
#
# # Define the path to your image
# image_path = 'pic\chickenFries.jpg'  # Change this to the path of your image
# image_path_out = '{}_out.jpg'.format(image_path)
#
# # Load the image
# image = cv2.imread(image_path)
#
# # Load a model
# model_path = 'bestFoodTaste.pt'  # Path to your model
# model = YOLO(model_path)  # Load a custom model
#
# threshold = 0.1
#
# # Predict on the image
# results = model(image)[0]
#
# # Process detection results
# for result in results.boxes.data.tolist():
#     x1, y1, x2, y2, score, class_id = result
#
#     if score > threshold:
#         cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
#         cv2.putText(image, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
#
# # Save the output image
# cv2.imwrite(image_path_out, image)
