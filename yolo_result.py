
from ultralytics import YOLO

import nutritionalValue

# Load a pretrained model
model = YOLO('best.pt')
threshold=0.4

def yolo_predict(img_path=r"pic/friedchicken-rice.jpg"):

    # Run Inference on the source
    resultss = model(source=img_path, show=False, conf=threshold, save=True) # generator of Results objects
    path=resultss[0].save_dir
    matrix=[]
    for results in resultss:
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            class_id = int(class_id)
            name=results.names[int(class_id)]
            value=nutritionalValue.dicData[name]
            num_col=0
            value=[name]+[num_col]+value
            matrix.append(value)
    total_col=0
    return matrix,path,total_col