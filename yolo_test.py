import cv2
from ultralytics import YOLO

# Load a pretrained model
model = YOLO('models/best.pt')

image = cv2.imread('Original pictures\img_11.png')
# Run Inference on the source
resultss = model(source='Original pictures\img_11.png', show=True, conf=0.4, save=True) # generator of Results objects
print(resultss)
# for result in results:
#     # If result contains detections, you might need to access attributes or keys directly.
#     # This is a generic way to print available information in `result` to understand its structure.
#     print(dir(result))
#     detected_classes = result.names
#     print("Detected Classes:", detected_classes)

for results in resultss:
# ציור מלבן סביב כל אובייקט שזוהה וכתיבת שם האובייקט
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > 0.2:
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(image, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

# שמירת התמונה המעובדת
cv2.imwrite('after_new.jpg', image)