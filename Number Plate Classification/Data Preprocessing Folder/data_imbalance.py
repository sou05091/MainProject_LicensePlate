import os
from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

def datagen(folder_name,num_augmented_images):
    # 데이터 증강 이미지 저장
    # 원본 이미지 디렉토리 경로
    original_image_dir = './dataset/train/' + folder_name

    # 데이터 증강된 이미지를 저장할 디렉토리 경로
    augmented_image_dir = './dataset/datagen/' + folder_name

    # ImageDataGenerator 설정
    datagen = ImageDataGenerator(
        rescale=1.0/255.,
        rotation_range=2,         # 회전 각도 범위 설정
        width_shift_range=0.07,    # 가로 이동 범위 설정
        height_shift_range=0.07,   # 세로 이동 범위 설정
        shear_range=0.07,          # 전단 강도 범위 설정
        zoom_range=0.07,           # 확대/축소 범위 설정
        #horizontal_flip=True,     # 수평 반전 여부
        fill_mode='nearest'       # 새로운 픽셀 채우는 방식
    )

    # 원본 이미지 파일 목록
    original_image_files = os.listdir(original_image_dir)

    # 데이터 증강 작업을 수행하고 저장하는 반복문
    for original_image_file in original_image_files:

        # 원본 이미지를 불러옴
        original_img_file = os.path.join(original_image_dir, original_image_file)
        original_image = Image.open(original_img_file)
        original_image = np.array(original_image)

        # 데이터 증강 작업을 수행하고 이미지를 생성
        augmented_images = []
        for i in range(num_augmented_images):
            augmented_image = datagen.random_transform(original_image)
            augmented_images.append(augmented_image)

        # 생성된 이미지를 저장
        base_filename, _ = os.path.splitext(original_image_file)
        for i, augmented_image in enumerate(augmented_images):
            augmented_image_path = os.path.join(augmented_image_dir)
            if not os.path.exists(augmented_image_path):
                os.makedirs(augmented_image_path)
            saved_image = os.path.join(augmented_image_path, f'{base_filename}_aug_{i}.jpg')
            augmented_image = Image.fromarray(augmented_image)
            augmented_image.save(saved_image)

    print(f'{len(original_image_files)}개의 원본 이미지에서 {num_augmented_images}개의 데이터 증강 이미지를 각각 저장했습니다.')

train_data_path = "./dataset/train/"
train_data = os.listdir("./dataset/train/")

for folder_name in train_data:
    check_folder = os.path.join(train_data_path, folder_name)
    num_files = len(os.listdir(check_folder))
    
    if num_files < 300:
        print(f"Folder {folder_name} has {num_files} files.")
        # 데이터 증강 작업을 수행할 횟수
        num_augmented_images = 1
        datagen(folder_name,num_augmented_images)
    elif 100 < num_files < 500:
        print(f"Folder {folder_name} has {num_files} files.")
        #num_augmented_images = 1
        #datagen(folder_name,num_augmented_images)
    elif num_files >= 500:
        print(f"Folder {folder_name} has {num_files} files.")
