import os

from PIL import Image

UNIT_SIZE = 229 # 图像的高

TARGET_WIDTH = 6 * UNIT_SIZE # 一行有6个图像，那么是6*229那么宽

path = "/home"

imagefile = []

for root, dirs, files in os.walk(path):

    for f in files :

        imagefile.append(Image.open(path+'/'+f))

        target = Image.new('RGB', (TARGET_WIDTH, UNIT_SIZE*3)) # 最终拼接的图像的大小为(229*3) * (229*6)

        left = 0

        right = UNIT_SIZE

        for image in imagefile:

            target.paste(image, (0, left, TARGET_WIDTH, right))

            left += UNIT_SIZE # 从上往下拼接，左上角的纵坐标递增

            right += UNIT_SIZE#左下角的纵坐标也递增

            quality_value = 100

            target.save(path+'/result.jpg', quality = quality_value)