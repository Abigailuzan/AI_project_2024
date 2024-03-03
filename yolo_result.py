import cv2
from ultralytics import YOLO

import os

dic={'AW cola':['Sodium, carbohydrate',40.61 ], 'Beijing Beef':['Fat, sodium, cholesterol, carbohydrate, protein', 301.89 ] ,'Chow Mein':['Fat, sodium, cholesterol, carbohydrate, protein, calcium, iron, potassium, vitamin D',162.98], 'Fried Rice':['Fat, carbohydrates, protein, calcium, iron, potassium',173.72], 'Hashbrown':['Fat, carbohydrate, protein, potassium',217.39], 'Honey Walnut Shrimp':['Fat, carbohydrates, protein potassium',271], 'Kung Pao Chicken':['Fat, carbohydrate,protein, iron, calcium, vitamin D, vitamin B6, magnesium, cobalanin, potassium, vitamin C, sodium,',129], 'String Bean Chicken Breast':['Fat, sodium, cholesterol, carbohydrate, protein, calcium, iron, potassium',122.99], 'Super Greens':['Fat, sodium, carbohydrate, protein',367.44], 'The Original Orange Chicken':['Fat, sodium, cholesterol, carbohydrate, protein,  potassium',323.34], 'White Steamed Rice':['Fat, carbohydrates, protein, calcium, iron, potassium',129.75], 'black pepper rice bowl':['Fat, sodium, carbohydrate, protein, potassium, calcium, iron',123.45], 'burger':['Fat, sodium, cholesterol, carbohydrate, protein, calcium, iron, potassium',221.24], 'carrot_eggs':['Fat, sodium, cholesterol, carbohydrate, protein, vitamin A, vitamin E',125.86], 'cheese burger':['Fat, sodium, cholesterol, carbohydrate, protein, calcium, iron, potassium, vitamin D',268.84], 'chicken waffle':['Fat, sodium, cholesterol, carbohydrate, protein, calcium, iron, potassium, vitamin D',294.19], 'chicken_nuggets':['Fat, carbohydrate,protein, iron, calcium, vitamin D, vitamin B6, magnesium, cobalanin, potassium',296], 'chinese_cabbage':['Sodium, carbohydrate, protein,calcium, iron, potassium', 12.86], 'chinese_sausage':['Fat, sodium, cholesterol, carbohydrate, protein',285.71 ], 'crispy corn':['Fat, sodium, carbohydrate, protein',440], 'curry':['Fat, sodium, cholesterol, carbohydrate, protein, calcium, iron, potassium',103.40], 'french fries':['Fat, sodium, carbohydrate, protein, calcium, iron, potassium',208.57 ], 'fried chicken':['Fat, carbohydrate,protein, iron, calcium, vitamin D, vitamin B6, magnesium, cobalanin',297], 'fried_chicken':['Fat, carbohydrate,protein, iron, calcium, vitamin D, vitamin B6, magnesium, cobalanin',297], 'fried_dumplings':['protein, carbohydrates, fat',356], 'fried_eggs':['Fat, sodium, cholesterol, carbohydrate, protein, vitamin D, calcium, iron, potassium',195.65], 'mango chicken pocket':['Fat, sodium, carbohydrate, protein, calcium, iron, potassium',97.73], 'mozza burger':['carbohydrates, protein, fat, cholesterol, sodium, vitamin A and C, Iron',284.40], 'mung_bean_sprouts':['Sodium, carbohydrate, protein, calcium, iron, potassium', 20.97], 'nugget':['fat, cholesterol, sodium, carbohydrates, fiber, protein', 180], 'perkedel':['Fat, sodium, cholesterol, carbohydrate, protein, calcium, iron, potassium, vitamin D',209.09], 'rice':['fat, carbs, protein',129], 'sprite':['Sodium, carbohydrate',41.04], 'tostitos cheese dip sauce':['Fat, sodium, carbohydrate, protein, potassium, iron',301.20], 'triangle_hash_brown':['Fat, carbohydrate, protein and potassium',217.39], 'water_spinach':['sodium, carbohydrate, protein, potassium, calcium, iron',19.64]}

# Load a pretrained model
model = YOLO('best.pt')
threshold=0.4

def yolo_predict(img_path=r"pic/friedchicken-rice.jpg"):

    # Run Inference on the source
    resultss = model(source=img_path, show=False, conf=threshold, save=True) # generator of Results objects
    #print(results)
    path=resultss[0].save_dir
    #print(f"path:{path}")
    names_pre=[]
    matrix=[]
    #print(results)
    for results in resultss:
        #boxes=result.boxes.cpu().numpy()

        #names_pre.append(result.names[int(boxes.cls[0])])
        #print(boxes.cls.shape[0])
       # for num in range(boxes.cls.shape[0]):
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            class_id = int(class_id)
            name=results.names[int(class_id)]
            #print(name)
            #print(type(name))
            value=dic[name]
            num_col=0
            value=[name]+[num_col]+value
            matrix.append(value)
    #print(matrix)
    #sum_list=sum(list)
    total_col=0
    return matrix,path,total_col
        #print(f"dic_value:{value}")
        #print(f"**:{int(boxes.cls[0])} type of:{type(boxes.cls)}")
    #print(matrix)
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
#yolo_predict()