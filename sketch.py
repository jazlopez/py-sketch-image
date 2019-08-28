import cv2
import sys
import os

source = sys.argv[1]
prefix = "sketch"

if len(sys.argv) >= 3:
    prefix = sys.argv[2]


real_path = os.path.realpath(source)
base_name = os.path.basename(real_path)
directory = os.path.dirname(real_path)
sketch_filename = "{}_{}".format(prefix, base_name)
sketch_path = os.path.join(directory, sketch_filename)

print(real_path)
print(base_name)
print(directory)
print(sketch_filename)

sk_gray, sk_color=cv2.pencilSketch(cv2.imread(source), sigma_s=60, sigma_r=0.07, shade_factor=0.05)
cv2.imwrite(sketch_path, sk_gray)
cv2.imshow(sketch_filename, cv2.imread(sketch_path))
cv2.waitKey(0)