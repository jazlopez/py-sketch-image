# py-sketch-image
Generate sketch version from images. It uses python3 and OpenCV to create sketch version of your image.

It works by creating a gray version of your image and applying a sketch effect to the new file. Sketch version of your image will be stored at the same directory of original image.

* Original image is not affected at all.

Example:

### ORIGINAL

  <img src="https://raw.githubusercontent.com/jazlopez/py-sketch-image/master/source.jpg">

#### SKETCH

  <img src="https://raw.githubusercontent.com/jazlopez/py-sketch-image/master/sketch_source.jpg">



#### 1. INSTALLATION

```
pip3 install -r requirements.txt
```

#### 2. USAGE

Run sketch.py providing the path of the image you want to sketch.

```
python3 sketch.py --source /image/path/to/original.png

# above command will create a new file in directory where sketch.png exists whose file name starts with default prefix "sketch_" plus the original file name:
# /image/path/to/original.png -> /image/path/to/sketch_original.png

# You can change the prefix to another string with the optional argument --prefix

python3 sketch.py --source /image/path/to/original.png --prefix new_sketch_

# output file: /image/path/to/new_sketch_original.png

# For advanced users you can set optional arguments to control SIGMA_S SIGMA_R SHADE_FACTOR:
python3 sketch.py --source original.png --sigma_s 9 --sigma_r 0.09 --shade 0.07 
```
#### 3. TODO:

-   Create image sketch version bulk mode

#### 4. VERSION

1.0.0   Initial

#### 5. CONTACT
If you have any idea on how to improve the software drop me a message at the link below.

<a href="jazlopez@github.com">Jaziel Lopez, Software Engineer</a>

> *DISCLAIMER:* Be aware the softtware is provided as is without any support nor liability in any country and/or jurisdiction. Do not contact the author with complains and/or legal issues you may think the author is responsible of. In all time software author is not responsible for others actions.
