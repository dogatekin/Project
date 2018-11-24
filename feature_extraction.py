import cv2
import math
import colorgram
import numpy as np


def calculate_num_norm_keypoints(image):
    '''Calculate number of (normalized) keypoints.'''
    #
    fast = cv2.FastFeatureDetector_create()

    # Total keypoints with nonmax suppression
    kp = fast.detect(image,None)

    # Adjust for resolution
    resolution = image.shape[0]*image.shape[1]

    # Derive and return number of norm keypoints
    return len(kp)/resolution


def calculate_entropy(image):
    '''Calculate entropy of image (degree of randomness).'''
    # Convert image to greyscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate frequency of pixels in range 0-255
    histogram = cv2.calcHist([gray_image],[0],None,[256],[0,256])
    pixels = sum(histogram)

    samples_probability = [float(h) / pixels for h in histogram]

    return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])[0]


def calculate_brightness(image):
    '''Calculate brightness of image.'''
    # Convert image to greyscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate frequency of pixels in range 0-255
    histogram = cv2.calcHist([gray_image],[0],None,[256],[0,256])

    # Sum ...
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else (brightness / scale)[0]


def calculate_colorfulness(image):
    '''Calculate colorfulness metric of image.'''
    # Split the image into its respective RGB components
    (B, G, R) = cv2.split(image.astype("float"))

    # Compute rg = R - G
    rg = np.absolute(R - G)

    # Compute yb = 0.5 * (R + G) - B
    yb = np.absolute(0.5 * (R + G) - B)

    # Compute the mean and standard deviation of both rg and yb
    (rb_mean, rb_std) = (np.mean(rg), np.std(rg))
    (yb_mean, yb_std) = (np.mean(yb), np.std(yb))

    # Combine the mean and standard deviations
    std_root = np.sqrt((rb_std ** 2) + (yb_std ** 2))
    mean_root = np.sqrt((rb_mean ** 2) + (yb_mean ** 2))

    # Derive the "colorfulness" metric and return it
    return std_root + (0.3 * mean_root)


# https://stackoverflow.com/questions/4801366/convert-rgb-values-to-integer/4801397
def calculate_top_colors(path, num_colors):
    '''Extract top 5 colors from image.'''
    col = colorgram.extract(path, num_colors)
    c = [0]
    # Covert RGB representation to one metric
    for i in range(num_colors):
        r, g, b = col[i].rgb
        #rgb = col[i].rgb[0]
        #rgb = (rgb << 8) + col[i].rgb[1]
        #rgb = (rgb << 8) + col[i].rgb[2]
        c.extend([r, g, b])
    # rgb = [[col[i].rgb[0],  col[i].rgb[1], col[i].rgb[2]] for i in range(num_colors)]
    return c[1:]

def calculate_num_unique_colors(image):
    '''Calculate number of unique colors in image.'''
    #len(set( tuple(v) for m2d in path for v in m2d ))
    # Derive and return
    return len(np.unique(image.reshape(-1, image.shape[2]), axis=0))
