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

#app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"


@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return

        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        results = model([img])

        results.render()  # updates results.imgs with boxes and labels
        target_class_index = 1
        confidence_threshold = 0.2  # 신뢰도
        for detection in results.pred[0]:
            x_min, y_min, x_max, y_max, confidense, class_num = detection
            print(detection)
            if (detection is not None
                and confidense >= confidence_threshold 
                and class_num == target_class_index):
                x_min = int(x_min)
                y_min = int(y_min)
                x_max = int(x_max)
                y_max = int(y_max)
                img_with_box = img.crop((x_min, y_min, x_max, y_max))
                now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
                img_savename = f"static/{now_time}.jpg"
                img_with_box.save(img_savename)
                return redirect(img_savename)
        return "No object detected."
    return render_template("index.html")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

    model = torch.hub.load('ultralytics/yolov5','custom',path='./weights/yolov5_license_plate.pt')  # force_reload = recache latest code
    model.eval()
    app.run(host="0.0.0.0", port=args.port)  # debug=True causes Restarting with stat