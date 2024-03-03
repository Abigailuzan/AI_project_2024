import cv2
from ultralytics import YOLO

import calories_list

image_path = 'Original pictures/img_4.png'
image = cv2.imread(image_path)
# Load a pretrained model
model = YOLO('best.pt')
threshold = 0.4

# Run Inference on the source
resultss = model(source=image_path, show=True, conf=threshold,save=True )  # generator of Results objects

for results in resultss:
    # ציור מלבן סביב כל אובייקט שזוהה וכתיבת שם האובייקט
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(image, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

# שמירת התמונה המעובדת
cv2.imwrite('תמונות מעובדות/image_out4.jpg', image)


'''
def calculate_resolution(image_path):
    # קריאת התמונה
    image = cv2.imread(image_path)
    # קביעת הרזולוציה
    resolution = image.shape[:2]  # רזולוציה היא הגובה והרוחב של התמונה
    return resolution


# דוגמא לקוד שמחשב כמה ריבועים 5x5 נכנסים בכל ריבוע שהמודל זיהה
for results in resultss:
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        
        class_id = int(class_id)  # int number instead of a float number for the index of the categori list
        calori_item_mili = calories_list.calories.get(class_id, None)
        # חישוב אורך ורוחב הריבוע שהמודל זיהה
        box_width = x2 - x1
        box_height = y2 - y1
        # חישוב כמה ריבועים 5x5 נכנסים בריבוע
        image_resolution = calculate_resolution(image_path)  #
        num_squares_width = box_width / 2.83
        num_squares_height = box_height / 2.83

        # חישוב השטח הכולל של ריבועים 5x5 שנכנסים
        total_squares = num_squares_width * num_squares_height

        # הדפסת המידע לכל ריבוע שזוהה
        print(
            f"Object Class: {results.names[int(class_id)]}, Bounding Box: {(x1, y1, x2, y2)}, 5x5 Squares Fitting: {total_squares}")
'''