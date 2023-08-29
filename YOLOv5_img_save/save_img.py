import io
import datetime
import torch
from PIL import Image
import os
import uuid

def predict_image(file_path, model):
    img = Image.open(file_path)
    results = model([img])  # 모델에 이미지 전달하여 결과 받기
    results.render()
    target_class_index = 1
    confidence_threshold = 0.2
    for detection in results.pred[0]:
        x_min, y_min, x_max, y_max, confidence, class_num = detection
        if (
            detection is not None
            and confidence >= confidence_threshold 
            and class_num == target_class_index
        ):
            x_min = int(x_min)
            y_min = int(y_min)
            x_max = int(x_max)
            y_max = int(y_max)
            img_with_box = img.crop((x_min, y_min, x_max, y_max))
            #now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
            img_savename = f"yolo_results/{uuid.uuid4()}.jpg"
            img_with_box.save(img_savename)
            return img_savename
    return None

if __name__ == "__main__":
    folder_path = "./test"  # 테스트할 폴더 경로
    model = torch.hub.load('ultralytics/yolov5','custom',path='./weights/yolov5_license_plate.pt')  # force_reload = recache latest code
    model.eval()
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            file_path = os.path.join(folder_path, filename)
            result_img = predict_image(file_path, model)
            if result_img:
                print(f"Detected object saved as: {result_img}")
            else:
                print("No object detected.")
