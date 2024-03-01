import cv2
from ultralytics import YOLO

image_path = 'Original pictures/img_13.png'
image = cv2.imread(image_path)
# Load a pretrained model
model = YOLO('models/best.pt')
threshold = 0.1

# Run Inference on the source
resultss = model(source=image_path, show=True, conf=threshold )  # generator of Results objects
for results in resultss:
    # ציור מלבן סביב כל אובייקט שזוהה וכתיבת שם האובייקט
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(image, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

# שמירת התמונה המעובדת
cv2.imwrite('Original pictures/image_out17.jpg', image)
