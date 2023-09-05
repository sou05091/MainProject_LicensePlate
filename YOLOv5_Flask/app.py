# """
# Simple app to upload an image via a web form 
# and view the inference results on the image in the browser.
# """
import argparse
import io
import os
from PIL import Image
import datetime
import torch
from flask import Flask, render_template, request, redirect
from flask import jsonify
from tempfile import NamedTemporaryFile
import model2_esrgan_super_resolution as esrgan
import model3_easy_ocr as ocr
import model4_roboflow_license_number_extractor as robo
import model1_img_classfication as vgg
import model_YOLOv5 as yolo

#app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"

# 번호판 짤린 이미지
#after_img_file_name = 저장된 곳으로 부터 읽어드림

# 현장 사진 
# original_img_file_name = 입력 받아야 함

# 번호판 짤린 이미지 저장할 폴더 경로
img_savefolder ="./test1"

# 이미지 이름
file_name = "0da9c411-72f1-42ce-b451-ea9208f9c761.jpg"
# 이미지 흑백 변경전 이미지
before_path = f"./license_plate/{file_name}"
# 이미지 흑백 변경후 이미지
after_path = f"./super_resolution/{file_name}"


@app.route("/", methods=["GET","POST"])
def process_all():
    if request.method == "POST":
        if "file" not in request.files:
            return jsonify({"error": "No file part"})

        file = request.files["file"]
        if not file:
            return jsonify({"error": "No selected file"})

        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))

        # Step 1: YOLOv5
        with NamedTemporaryFile(delete=False, suffix=".jpg") as temp_img_file:
            temp_img_file.write(img_bytes)
            temp_img_file_name = temp_img_file.name
            file_name = yolo.YOLOv5_Load(temp_img_file_name, img_savefolder)
        
        file_path_name = f"./{file_name}"
        # Step 2: Plate Preprocessing (Super-Resolution)
        esrgan.model_result(file_path_name, after_path)

        # Step 3: Number Result 1 (VGG)
        vgg_result = vgg.model_result(file_path_name)

        # Step 4: Number Result 2 (OCR)
        ocr_result = ocr.model_result(after_path)

        # Step 5: Number Result 3 (License Number Extraction)
        robo_result = robo.model_result(after_path)

        return jsonify({
            #"super_resolution_image": super_res_img.tostring(),
            "vgg_result": vgg_result,
            "ocr_result": ocr_result,
            "robo_result": robo_result
        })
        #return redirect()
    return render_template("index.html")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=args.port)  # debug=True causes Restarting with stat