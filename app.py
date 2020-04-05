
import numpy as np
import cv2
from pprint import pprint
import json
import io
import base64
import os
import logging
from flask import request
from flask_api import FlaskAPI, status
from flask_cors import CORS
from functional.file_helpers import FileHelpers
from functional.cv.image_duplicates import ResizeImage
from functional.cv.template_detection import TemplateDetection
from PIL import Image

app = FlaskAPI(__name__)
CORS(app)

@app.route('/temp_detect/', methods=['POST'])
def temp_detect():
    try:
        # print("ENTERED HERE")
        # print(request.headers)
        # print(request)
        r = request
        # pprint(request.__dict__)
        # print(json.dumps(request.json))
        # print(request.json)
        # print(type(request.json))
        im = request.json["img"]
        print(im)
        # im = im.encode("utf-8")
        offset = im.index(',')+1
        img_bytes = base64.b64decode(im[offset:])

        # img_bytes = base64.b64decode(im)
        img = Image.open(io.BytesIO(img_bytes))
        img = np.array(img)

        # image_64_decode = base64.decodestring(im)
        # image_result = open("other_im.jpg", 'wb')
        # image_result.write(image_64_decode)
        # fh = open("imageToSave.jpg", "wb")
        # fh.write(im.decode('base64'))
        # fh.close()
        # nparr = np.fromstring(request.json["img"], np.uint8)
        # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # print("After this")
        # print(request.data)
        # print(request.files)
        # to_eval_img = request.files.get('img')
        # print(to_eval_img)
        temp_det = TemplateDetection()
        (startX, startY, endX, endY) = temp_det.detect(img)

        # image = Image.open(io.BytesIO(im))
        # image.save("other_img.jpg")

        return {'startX': startX, 'startY': startY, 'endX': endX, 'endY': endY}, status.HTTP_200_OK
    except:
        logging.exception("Got exception")
        return {'success': False}, status.HTTP_400_BAD_REQUEST

@app.route('/add_img_temp/', methods=['POST'])
def add_img_temp():
    try:

        pprint(request.__dict__)

        temp_folder = FileHelpers.get_or_create_folder()

        temp_img = request.files.get('temp_img')
        # model_3d = request.files.get('model_3d')
        # if not temp_img or not model_3d:
        #     return status.HTTP_400_BAD_REQUEST

        temp_img.save(os.path.join(temp_folder, temp_img.filename))
        # model_3d.save(os.path.join(temp_folder, model_3d.filename))

        ResizeImage.create_img_duplicates(os.path.join(temp_folder, temp_img.filename), temp_folder)
        return {'success': True}, status.HTTP_200_OK
    except:
        logging.exception("Got exception")
        return {'success': False}, status.HTTP_400_BAD_REQUEST

if __name__ == '__main__':
    app.run(debug=True)
