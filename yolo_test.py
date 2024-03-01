from numpy.ma.bench import timer
from ultralytics import YOLO

# Load a pretrained model
model = YOLO('bestFoodTaste100.pt')

# Run Inference on the source
results = model(source='pic/friedchicken-rice.jpg', show=True, conf=0.1, save=True) # generator of Results objects
print(results)
# for result in results:
#     # If result contains detections, you might need to access attributes or keys directly.
#     # This is a generic way to print available information in `result` to understand its structure.
#     print(dir(result))
#     detected_classes = result.names
#     print("Detected Classes:", detected_classes)