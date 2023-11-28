import cv2
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import urllib.request
import numpy as np
def resize_img(img):
    req = urllib.request.urlopen(img)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    super_res = cv2.dnn_superres.DnnSuperResImpl_create()
    super_res.readModel(f'{BASE_DIR}/posts/LapSRN_x4.pb')
    super_res.setModel('lapsrn', 4)
    lapsrn_image = super_res.upsample(image)
    filename = f'{BASE_DIR}/media/images/designs/'+str (img.split('/')[-1])
    cv2.imwrite(filename,lapsrn_image)
    print(filename)
    return filename
