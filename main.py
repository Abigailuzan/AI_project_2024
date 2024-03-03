import cv2
from ultralytics import YOLO
import calories_list

# image_path = 'Original pictures/img_4.png'
# image = cv2.imread(image_path)
# Load a pretrained model
# model = YOLO('best.pt')
# threshold = 0.4

# Run Inference on the source
# resultss = model(source=image_path, show=True, conf=threshold, save=True)  # generator of Results objects

Total_calories = []
# Function to sum Total_calories
def sum_total_calories():
    return sum(Total_calories)

# Function to empty the Total_calories list
def reset_total_calories():
    Total_calories.clear()
'''
def calculate_resolution(image_path):
    imag = cv2.imread(image_path)
    resolution = imag.shape[:2]
    return resolution
for results in resultss:
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        class_id = int(class_id)  # int number instead of a float number for the index of the categori list
        calori_item_mili = calories_list.calories.get(results.names.get(class_id))
        if calori_item_mili is None:
            print('no element found')
            break
            #return 0
        box_width = x2 - x1
        box_height = y2 - y1
        image_height, image_width = calculate_resolution(image_path)
        num_squares_width = box_width/3.78
        num_squares_height = box_height / 3.78
        total_squares = num_squares_width * num_squares_height
        total_calories = total_squares * calori_item_mili[0] * calori_item_mili[1]
        Total_calories.append(total_calories)
        print(total_calories)
        #return total_calories
print(sum(Total_calories))
'''


#def Calories_Calculator(image_path, x1, y1, x2, y2, class_id, results):
def Calories_Calculator( x1, y1, x2, y2, name):
    calori_item_mili = calories_list.calories.get(name)
    if calori_item_mili is None:
        print('no element found')
        return 0
        # return 0
    box_width = x2 - x1
    box_height = y2 - y1
    # image_height, image_width = calculate_resolution(image_path)
    num_squares_width = box_width / 3.78
    num_squares_height = box_height / 3.78
    total_squares = num_squares_width * num_squares_height
    total_calories = total_squares * calori_item_mili[0] * calori_item_mili[1]
    Total_calories.append(total_calories)
    return total_calories
