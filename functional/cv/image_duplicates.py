
import os
import cv2
from PIL import Image

class ResizeImage:

    @staticmethod
    def create_img_duplicates(img_path, temp_path):
        sizes = [(10, 10), (20, 20), (40, 40), (80, 80), (160, 160)]
        if os.path.isfile(img_path):
            im = Image.open(img_path)
            for size in sizes:
                print("X1")
                f, e = os.path.splitext(img_path)
                imResize = im.resize(size, Image.ANTIALIAS)
                imResize = imResize.convert('RGB')
                imResize.save(os.path.join(temp_path, f"{size[0]}new_name{size[1]}.jpg"), "JPEG", quality=90)
