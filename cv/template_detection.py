import cv2
import numpy as np

class TemplateDetection:
    def __init__(self):
        # self.img_url = img_url
        self.templates = self.get_templates()
        self.threshold = 0.75
        self.temp_match_algo = cv2.TM_CCOEFF_NORMED

    def detect(self, img):
        to_detect_img = cv2.imread(img)
        img_gray = cv2.cvtColor(to_detect_img, cv2.COLOR_BGR2GRAY)

        for template in self.templates:
            temp_w, temp_h = template.shape[::-1]
            found = None
            for scale in np.linspace(0.2, 1.0, 20)[::-1]:

                edged = cv2.Canny(resized, 50, 200)
                result = cv2.matchTemplate(edged, template, self.temp_match_algo)
                (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

                resized = imutils.resize(img_gray, width=int(img_gray.shape[1] * scale))
                r = img_gray.shape[1] / float(resized.shape[1])

                if resized.shape[0] < temp_h && resized.shape[1] < temp_w:
                    break
                found = (maxVal, maxLoc, r)

        (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
        (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

        return (startX, startY, endX, endY)
        # res = cv2.matchTemplate(img_gray, template, self.temp_match_coeff)

    def get_templates(self):
        pass
