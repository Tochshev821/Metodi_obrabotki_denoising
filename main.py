
import pydicom
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pylab

def viewImage(image):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def print_hi(name):
    a=2
    img = cv2.imread('pic5295.jpg')

    #viewImage(img)
    print("Image Properties")
    print("- Number of Pixels: " + str(img.size))
    print("- Shape/Dimensions: " + str(img.shape))

    # Read image
    img = cv2.imread('pic5295.jpg', 0)

    # Perform binary thresholding on the image with T = 125
    r, threshold = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
    #viewImage(threshold)

    # Create our sharpening kernel, the sum of all values must equal to one for uniformity
    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])

    # Applying the sharpening kernel to the grayscale image &amp; displaying it.
    print("\n\n--- Effects on S&amp;P Noise Image with Probability 0.5 ---\n\n")

    # Applying filter on image with salt &amp; pepper noise
    sharpened_img = cv2.filter2D(sp_05, -1, kernel_sharpening)
    viewImage(sharpened_img)

if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
