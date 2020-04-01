
import os
import cv2
from PIL import Image

class ResizeImage:

    @staticmethod
    def create_img_duplicates(img_path, img_item):
        sizes = [(10, 10), (20, 20), (40, 40), (80, 80), (160, 160)]
        if os.path.isfile(img_path+img_item):
            im = Image.open(img_path+img_item)
            for size in sizes:
                f, e = os.path.splitext(img_path)
                imResize = im.resize(size, Image.ANTIALIAS)
                imResize.save(f + f"{size[0]}{im.name}{size[1]}.jpg", "JPEG", quality=90)
