import os

def rename_folders_and_files(folder_path):
    # 현재 폴더 내의 파일 및 폴더 목록 가져오기
    contents = os.listdir(folder_path)
    
    for item in contents:
        item_path = os.path.join(folder_path, item)
        
        if os.path.isfile(item_path):  # 파일인 경우
            if not item.endswith(".jpg"):
                new_item_name = item + ".jpg"
                new_item_path = os.path.join(folder_path, new_item_name)
                os.rename(item_path, new_item_path)
            
        elif os.path.isdir(item_path):  # 폴더인 경우
            rename_folders_and_files(item_path)  # 재귀적으로 하위 폴더 내의 파일 및 폴더도 처리

# 상위 폴더 경로 설정
parent_folder_path = "./test"  # 상위 폴더 경로를 적절히 수정해주세요

rename_folders_and_files(parent_folder_path)

print("작업 완료!")
