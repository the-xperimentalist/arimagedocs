
import os
from flask_api import FlaskAPI, status
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug import secure_filename
from file_helpers import FileHelpers
from cv.image_duplicates import ResizeImage
from cv.template_detection import TemplateDetection

app = FlaskAPI(__name__)


@app.route('/temp_detect', methods=['POST'])
def temp_detect():
    to_eval_img = request.files.get('img')
    temp_det = TemplateDetection()
    (startX, startY, endX, endY) = temp_det.detect(to_eval_img)

    return {'startX': startX, 'startY': startY, 'endX': endX, 'endY': endY}, status.HTTP_200_OK

@app.route('/add_img_temp', methods=['POST'])
def add_img_temp(request):
    temp_folder = FileHelpers.get_or_create_folder()
    temp_img = request.files.get('temp_img')
    model_3d = request.files.get('model_3d')
    if not temp_img or not model_3d:
        return status.HTTP_400_BAD_REQUEST

    temp_img.save(temp_folder, temp_img.filename)
    model_3d.save(temp_folder, model_3d.filename)

    ResizeImage.create_img_duplicates(temp_folder, temp_img.filename)
    return {'success': True}, status.HTTP_200_OK

if __name__ == '__main__':
    app.run(debug=True)
