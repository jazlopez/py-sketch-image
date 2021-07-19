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
python3 sketch.py /image/path/to/sketch
```
#### 3. TODO:

- ~~argument parser / help option
- ~~skip display window after convert an image by default
- ~~fix blurrynes: update sigma_r, sigma_s and shade factor to produce better sketchy images by reducing the blurryness of the default values in the script.


#### 4. VERSION

1.0.0   Initial

#### 5. CONTACT
If you have any idea on how to improve the software drop me a message at the link below.

<a href="jazlopez@github.com]">Jaziel Lopez, Software Engineer</a>

> *DISCLAIMER:* Be aware the softtware is provided as is without any support nor liability in any country and/or jurisdiction. Do not contact the author with complains and/or legal issues you may think the author is responsible of. In all time software author is not responsible for others actions.
