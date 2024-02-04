from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

model = load_model('model/food_model1.h5')
# We will open the class list text file and read the class names into a list.
# Each line in the file corresponds to a class name.

# Path to the class list file
class_list_path = 'annot/class_list.txt'

# Read the class names into a list
with open(class_list_path, 'r') as file:
    class_names = [line.strip() for line in file.readlines()]

# Check the first few class names to ensure they have been read correctly
print(class_names[:5])

# Ensure the class_names list is correctly ordered before using it for prediction mapping
class_labels = {index: name.split(' ')[1] for index, name in enumerate(class_names)}  # Di

img_path = "test_set/test_003496.jpg"
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # Add a batch dimension
img_array /= 255.0  # Scale the image pixels to [0, 1]
prediction = model.predict(img_array)
predicted_class = np.argmax(prediction, axis=1)

predicted_class_index = np.argmax(prediction, axis=1)[0]  # Get the index of the highest probability
predicted_label = class_labels[predicted_class_index]  # Map the index to the class name
print("Predicted class:", predicted_label)



