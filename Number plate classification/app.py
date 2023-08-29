from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import tensorflow as tf

# Flask 애플리케이션 생성
app = Flask(__name__)

# 모델 로드 및 클래스 이름 설정
# 이 부분은 모델 로드와 클래스 이름 설정하는 부분으로 대체되어야 합니다.
class_names = ['CassFresh', 'budweiser', 'filite', 'hineken', 'jinro']  # 예시 클래스 이름

@app.route('/', methods=['GET', 'POST'])
def upload_predict():
    if request.method == 'POST':
        # 업로드한 이미지 처리
        image_file = request.files['image']
        if image_file:
            img = Image.open(image_file)
            img = img.resize((150,150))
            x = np.array(img)
            x = np.expand_dims(x, axis=0)
            x = x / 255.0

            # 모델로 예측 수행
            predictions = model.predict(x)[0]
            top_class_indices = np.argsort(predictions)[::-1][:3]
            
            prediction_results = []
            for class_index in top_class_indices:
                class_name = class_names[class_index]
                confidence = predictions[class_index] * 100
                prediction_results.append((class_name, confidence))

            return render_template('index.html', prediction_results = prediction_results)

    return render_template('index.html', prediction_results=[])

if __name__ == '__main__':
    # 모델 로드 및 초기화
    model = tf.keras.models.load_model('./complete_model.h5')  # 모델 로드 및 초기화 부분
    
    # Flask 애플리케이션 실행
    app.run(debug=True)
