import os
import shutil
from PIL import Image
import uuid
import torch

source_folder = "./20230710"  # 원본 폴더 경로
destination_folder = "./dataset"
length_folder = len(os.listdir(source_folder))

def copy_file():
    count = 1
    for folder_name in os.listdir(source_folder):
        folder_name = os.path.join(source_folder, folder_name)
        for license_plate_folder in os.listdir(folder_name):
            if license_plate_folder == "차량번호인식":
                license_plate_folder = os.path.join(folder_name, license_plate_folder)
                len_license_plate_folder = len(os.listdir(license_plate_folder))
                if len_license_plate_folder >= 15:
                    count += 1
                    for file_name in os.listdir(license_plate_folder):
                        if not os.path.exists(destination_folder):
                            os.makedirs(destination_folder)
                        source_file_path = os.path.join(license_plate_folder, file_name)
                        destination_file_path = os.path.join(destination_folder, str(count))
                        
                        # 이미지를 목적지 폴더로 복사
                        shutil.copy(source_file_path, destination_file_path)
                        print(f"{file_name} 파일이 {destination_file_path}로 복사되었습니다.")
                    
def make_folder():
    for i in range(1, length_folder):
        os.makedirs(f"./dataset/{i}")
        print(f"{i}폴더 생성 완료")
        
def add_extension_to_files():
    for folder_name in os.listdir(destination_folder):
        folder_path = os.path.join(destination_folder, folder_name)
        print(folder_path)
        for file_name in os.listdir(folder_path):
            print(file_name)
            old_file_path = os.path.join(folder_path, file_name)
            new_filename = f"{file_name}.jpg"
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f"{file_name} 파일 이름이 {new_filename}로 변경되었습니다.")

def YOLOv5(file_path, model, i):
    img = Image.open(file_path)
    results = model([img])  # 모델에 이미지 전달하여 결과 받기
    results.render()
    target_class_index = 1
    confidence_threshold = 0.3
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
            img_savefolder = f"./result/{i}"
            if not os.path.exists(img_savefolder):
                os.makedirs(img_savefolder)
            img_savename = f"./result/{i}/{uuid.uuid4()}.jpg"
            img_with_box.save(img_savename)
            return img_savename
    return None

def YOLOv5_Load():
    model = torch.hub.load('ultralytics/yolov5','custom',path='./weights/yolov5_license_plate.pt')  # force_reload = recache latest code
    model.eval()
    for i in range(1,length_folder):
        folder_path = f"./dataset/{i}"  # 로드할 이미지 폴더 경로
        if not os.path.exists(folder_path):
            print("None File")
        else:
            for filename in os.listdir(folder_path):
                if filename.endswith(".jpg"):
                    file_path = os.path.join(folder_path, filename)
                    result_img = YOLOv5(file_path, model, i)
                    if result_img:
                        print(f"Detected object saved as: {result_img}")
                    else:
                        print("No object detected.")
        
def main():
    make_folder()
    copy_file()
    add_extension_to_files()
    YOLOv5_Load()
    
if __name__ == "__main__":
    main()