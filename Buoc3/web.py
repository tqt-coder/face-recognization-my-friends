from flask import Flask, render_template, request
import os
from random import random
import cv2
import sys
import tkinter
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter.filedialog import Open, SaveAs

import numpy as np
import os.path
import cv2
import joblib
import sys
from sklearn.svm import LinearSVC

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/upload"


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/process", methods=['POST'])
def recognizeFace():
    try:
        image = request.files['file']
        print(image)
        if image:
            # Lưu file
            path_to_save = os.path.join(
                app.config['UPLOAD_FOLDER'], image.filename)
            print("Save = ", path_to_save)
            image.save(path_to_save)

        #     imgin = cv2.imread(path_to_save)
        #     width = 320
        #     height = 320  # keep original height
        #     dim = (width, height)
        #     # resize image
        #     imgin = cv2.resize(imgin, dim, interpolation=cv2.INTER_AREA)

        #     faces = detector.detect(imgin)
        #     face_align = recognizer.alignCrop(imgin, faces[1][0])
        #     face_feature = recognizer.feature(face_align)
        #     test_prediction = svc.predict(face_feature)

        #     result = mydict[test_prediction[0]]
        #     cv2.putText(imgin, result, (5, 15),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

        #     cv2.imwrite(path_to_save, imgin)

        #     # Trả về kết quả
            return render_template("index.html", user_image=image.filename, rand=str(random()),
                                   msg="Tải file lên thành công")

        else:
            return render_template('index.html', msg='Hãy chọn file để tải lên')

    except Exception as ex:
        print(ex)
        return render_template('index.html', msg=ex)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
