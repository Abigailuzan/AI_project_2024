import os
import pandas as pd
from PIL import Image


# Assume the structure of the UECFOOD256 dataset
dataset_dir = 'UECFOOD256'  # Update this path
#annotations_dir = os.path.join(dataset_dir, 'Annotations')  # Update based on actual structure
images_dir = os.path.join(dataset_dir, '1')  # Update based on actual structure
# Let's first read the content of the uploaded file to understand its current format.
file_path = 'UECFOOD256/1/bb_info.txt'
file_label = 'UECFOOD256/labels'
with open(file_path, 'r') as file:
    content = file.read()

# Display the content to get an idea of its structure
content=content.split('\n')
content=content[1:-1]
# print(content)
# print(type(content))
# print(content[0][1:-1])
# Function to convert bounding box from absolute to normalized YOLO format
# Function to normalize bounding box coordinates based on image dimensions
# def normalize_coordinates(left, top, right, bottom, image_width, image_height):
#     """
#     Normalize the bounding box coordinates.
#
#     Parameters:
#     - left: The x-coordinate of the left side of the bounding box (in pixels)
#     - top: The y-coordinate of the top side of the bounding box (in pixels)
#     - right: The x-coordinate of the right side of the bounding box (in pixels)
#     - bottom: The y-coordinate of the bottom side of the bounding box (in pixels)
#     - image_width: The width of the image (in pixels)
#     - image_height: The height of the image (in pixels)
#
#     Returns:
#     - A tuple of normalized coordinates (left, top, width, height)
#     """
#     norm_left = left / image_width
#     norm_top = top / image_height
#     norm_width = (right - left) / image_width
#     norm_height = (bottom - top) / image_height
#
#     return [norm_left, norm_top, norm_width, norm_height]





for line in content:
    line_arr=line.split()
    image_file=f'{line_arr[0]}.jpg'
    folder_path = '1'
    image_path = os.path.join(images_dir, image_file)
    # image_size = Image.open(image_path).size  # PIL for image size
    # image_width, image_height=image_size
    # print(type(image_size[0]))
    box=line_arr[1:]
    left, top, right, bottom = map(float, box)
    # print(box)
    #bbox_normalized= normalize_coordinates(left, top, right, bottom,image_width, image_height )
    bbox_normalized.append(0)
    bbox_normalized=bbox_normalized[::-1]
    my_array_str = [str(element) for element in bbox_normalized]
    # Then, join them with a space as the separator
    my_string = " ".join(my_array_str)
    text_file = f'{line_arr[0]}.txt'

    # Create the directory if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    #Write to a new file for each image
    label_dir = os.path.join(file_label, text_file)
    with open(label_dir, 'w') as f:
           f.write(f"{my_string}")
# for image_file in os.listdir(images_dir):
#     if image_file.endswith('.jpg') :
#         image_path = os.path.join(images_dir, image_file)
# Iterate through annotation files and convert them
# for annotation_file in os.listdir(annotations_dir):
#     filepath = os.path.join(annotations_dir, annotation_file)
#     # Assuming CSV or similar structured annotation; adjust based on actual format
#     df = pd.read_csv(filepath, header=None)
#     image_id = annotation_file.split('.')[0]
#     image_path = os.path.join(images_dir, f'{image_id}.jpg')
#     image_size = Image.open(image_path).size  # PIL for image size
#
#     yolo_format_lines = []
#     for index, row in df.iterrows():
#         class_id = row[0]  # Update based on actual column containing class_id
#         bbox = [row[1], row[2], row[3], row[4]]  # Update based on actual columns for bbox
#         bbox_normalized = convert_bbox(image_size, bbox)
#
#         yolo_format_lines.append(f"{class_id} {' '.join(map(str, bbox_normalized))}")
#
#     # Write to a new file for each image
#     with open(f'{image_path.replace(".jpg", ".txt")}', 'w') as f:
#         for line in yolo_format_lines:
#             f.write(f"{line}\n")
