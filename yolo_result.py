import cv2
from ultralytics import YOLO
from main import Calories_Calculator, sum_total_calories, reset_total_calories
import os
import nutritionalValue

# Load a pretrained model
model = YOLO('best.pt')
threshold=0.4

def yolo_predict(img_path=r"pic/friedchicken-rice.jpg"):
    #Total_calories=[]
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
            value=nutritionalValue.dicData[name]
            num_col=Calories_Calculator( x1, y1, x2, y2,name)
            num_col=round(num_col, 2)
            value=[name]+[num_col]+value
            matrix.append(value)
    #print(matrix)
    #sum_list=sum(list)
    total_col= round(sum_total_calories(),2)
    reset_total_calories()
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