import cv2
import time
import filetype
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--source", required=True, help="Path to file image to create a sketch version from")
parser.add_argument("--prefix", required=False, default="sketch_", help="String used to prefix output file name")
parser.add_argument("--sigma_s", type=float, required=False, default=90, help="Sigma_S value between 0-100")
parser.add_argument("--sigma_r", type=float, required=False, default=0.09, help="Sigma_R value between 0-0.1")
parser.add_argument("--shade", type=float, required=False, default=0.09, help="Shade factor value between 0-0.1")

opts = parser.parse_args()

source = opts.source
PREFIX = opts.prefix
SIGMA_S= opts.sigma_s
SIGMA_R= opts.sigma_r
SHADE_FACTOR=opts.shade
real_path = os.path.realpath(source)

if 0 < SIGMA_S > 100:
    raise RuntimeError("Sigma_S value between 0-100")
if 0 < SIGMA_R > 0.1:
    raise RuntimeError("Sigma_R value between 0-0.1")
if 0 < SHADE_FACTOR > 0.1:
    raise RuntimeError("Shade factor value between 0-0.1")
if not os.path.exists(real_path):
    raise RuntimeError(f"Source file does not exist: {real_path}")

if not filetype.is_image(real_path):
    raise RuntimeError(f"{real_path} is not a valid image type. It could be damaged, corrupted or file is empty.")

base_name = os.path.basename(real_path)
directory = os.path.dirname(real_path)
sketch_filename = "{}_{}".format(PREFIX, base_name)
sketch_path = os.path.join(directory, sketch_filename)


cv2.namedWindow(sketch_filename, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(sketch_filename, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(sketch_filename, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_NORMAL)

sk_gray, sk_color=cv2.pencilSketch(cv2.imread(source), sigma_s=SIGMA_S, sigma_r=SIGMA_R, shade_factor=SHADE_FACTOR)
cv2.imwrite(sketch_path, sk_gray)

print("sketch version of your image written to: {}".format(sketch_path))
print("DO NOT CLOSE THE WINDOW....using your keyboard press any key to exit gracefully")
cv2.imshow(sketch_filename, cv2.imread(sketch_path))
cv2.waitKey(0)
cv2.destroyAllWindows()
print("good bye...")
exit(0)
