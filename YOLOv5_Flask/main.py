import model2_esrgan_super_resolution as esrgan
import model3_easy_ocr as ocr
import model4_roboflow_license_number_extractor as robo
import model1_img_classfication as vgg
import model_YOLOv5 as yolo
import model5_num_classification_YOLO as ncy
import model6_num_classifiaction_vgg as ncv

# 번호판 짤린 이미지
after_img_file_name = "./test1/9947ba3a-5bfe-438e-bf08-df46d1040b08.jpg"
# 현장 사진
original_img_file_name = "./test/test.jpg"
# 번호판 짤린 이미지 저장할 폴더 경로
img_savefolder ="./test1"

# 이미지 이름
file_name = "0da9c411-72f1-42ce-b451-ea9208f9c761.jpg"

# 이미지 흑백 변경전 이미지
before_path = f"./license_plate/{file_name}"
# 이미지 흑백 변경후 이미지
after_path = f"./super_resolution/{file_name}"



def main():
    # Step 1: YOLOv5
    #original_img_file_name = 로드할 이미지 파일 이름
    #img_savefolder = 저장할 이미지 폴더
    yolo.YOLOv5_Load(original_img_file_name, img_savefolder)
    
    # Step 2: Plate Preprocessing
    print()
    print("Preprocessing...")
    esrgan.model_result(after_img_file_name, after_path)    

    # Step 3: Number Result 1
    vgg.model_result(after_img_file_name)
    
    # Step 3: Number Result 2
    print()
    print("Model2 Result: ")
    ocr.model_result(after_path)

    # Step 4: Number Result 3    
    print()
    print("Model3 Result: ")    
    robo.model_result(after_path)
    print()
    
    # step 5: Number Classification Use YOLOv5 
    result = ncy.load_yolo(after_path)
    print(result)
    
    # 필요할 시 추가 예정
    # setp 6: Number Classification Use VGG16
    #ncv.classfication_number()
if __name__ == "__main__":
    main()