import os

folder_path = "./dataset/license_plate_number"  # 해당 폴더 경로로 수정하세요

for folder_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path,folder_name)
    for filename in os.listdir(file_path):
        if filename.endswith(".jpg"):
            delete_file_path = os.path.join(file_path, filename)
            print(delete_file_path)
            os.remove(delete_file_path)
            print(f"{filename} 파일이 삭제되었습니다.")
