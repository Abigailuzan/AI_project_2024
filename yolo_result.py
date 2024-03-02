import cv2
from ultralytics import YOLO

import os

dic={'AW cola':['Sodium and carbohydrate',40.61 ], 'Beijing Beef':['Fat, sodium, cholesterol, carbohydrate and protein', 301.89 ] ,'Chow Mein':['Fat, sodium, cholesterol, carbohydrate, protein, calcium, iron, potassium and vitamin D',162.98], 'Fried Rice':['Fat, carbohydrates, protein, calcium, iron and potassium',173.72], 'Hashbrown':[], 'Honey Walnut Shrimp':[], 'Kung Pao Chicken':[], 'String Bean Chicken Breast':[], 'Super Greens':[], 'The Original Orange Chicken':[], 'White Steamed Rice':[], 'black pepper rice bowl':[], 'burger':[], 'carrot_eggs':[], 'cheese burger':[], 'chicken waffle':[], 'chicken_nuggets':[], 'chinese_cabbage':[], 'chinese_sausage':[], 'crispy corn':[], 'curry':[], 'french fries':[], 'fried chicken':[], 'fried_chicken':[], 'fried_dumplings':[], 'fried_eggs':[], 'mango chicken pocket':[], 'mozza burger':[], 'mung_bean_sprouts':[], 'nugget':[], 'perkedel':[], 'rice':[], 'sprite':[], 'tostitos cheese dip sauce':[], 'triangle_hash_brown':[], 'water_spinach':[]}

# Load a pretrained model
model = YOLO('models/bestFoodTaste.pt')


# Run Inference on the source
results = model(source='Original pictures\img_11.png', show=True, conf=0.4, save=True) # generator of Results objects
print(results)
path=results[0].save_dir
print(f"path:{path}")
names_pre=[]
for result in results:
    boxes=result.boxes.cpu().numpy()
    names_pre.append(result.names[int(boxes.cls[0])])
    #print(f"**:{int(boxes.cls[0])} type of:{type(boxes.cls)}")
print(names_pre)
#print(type(results))
# Use the function to get the latest results path
#results_path = find_latest_results_path()
#print(f"The latest results are saved in: {results_path}")
# Detected classes and their details
#detected_classes = results.names
#print(f"The detected classes are: {detected_classes}")
#len_my=len(results)
#print(f"the length:{len_my}")
#for item in results:

  #  print(item)
 #   print("****\n")

#print(f"results: {results.pred[0]}")