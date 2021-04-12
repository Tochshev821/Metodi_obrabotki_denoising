from skimage import io
from scipy import ndimage as nd
import pydicom
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pylab
from scipy.ndimage import maximum_filter, minimum_filter
from matplotlib import pyplot as plt


# отыскать источник порождения артефактов (источник вторичных волн
# четко находить источник!!!
# пн или вт или в конце недели
# полярная система координат попробовать преобразить

def viewImage(image):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def print_hi(name):
    #пытался найти и выделить артефакт
    # # read image as grayscale
    # img = cv2.imread('pic5295.jpg')
    # hh, ww = img.shape[:2]
    #
    # # shave off white region on right side
    # img = img[0:hh, 0:ww - 2]
    #
    # # convert to gray
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #
    # # median filter
    # median = cv2.medianBlur(gray, 3)
    #
    # # do canny edge detection
    # canny = cv2.Canny(median, 100, 200)
    #
    # # get canny points
    # # numpy points are (y,x)
    # points = np.argwhere(canny > 0)
    #
    # # get min enclosing circle
    # center, radius = cv2.minEnclosingCircle(points)
    # print('center:', center, 'radius:', radius)
    #
    # # draw circle on copy of input
    # result = img.copy()
    # x = int(center[1])
    # y = int(center[0])
    # rad = int(radius)
    # cv2.circle(result, (x, y), rad, (255, 255, 255), 1)
    #
    # # write results
    # cv2.imwrite("sunset_canny.jpg", canny)
    # cv2.imwrite("sunset_circle.jpg", result)
    #
    # # show results
    # cv2.imshow("median", median)
    # cv2.imshow("canny", canny)
    # cv2.imshow("result", result)
    # cv2.waitKey(0)

 #    img = cv2.imread('pic5295.jpg')
 #
 #    #viewImage(img)
 #    print("Image Properties")
 #    print("- Number of Pixels: " + str(img.size))
 #    print("- Shape/Dimensions: " + str(img.shape))
 #
 #    # Read image
 #    #img = cv2.imread('pic5295.jpg', 0)
 #    viewImage(img)
 #
 #        # try to denoise with skimage
 #    # gausian_img=nd.gaussian_filter(img, sigma=3)
 #    # viewImage(gausian_img)
 #    # mid_img=nd.median_filter(img, size=7)
 #    # viewImage(mid_img)
 #    # min_img=nd.minimum_filter(img, size=4)
 #    # viewImage(min_img)
 #
 #
 #    # Perform binary thresholding on the image with T = 125
 #    # r, threshold = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
 #    # viewImage(threshold)
 #
 #            # Арифметический фильтр с Sharpening Kernel
 #    # Create our sharpening kernel, the sum of all values must equal to one for uniformity
 #    kernel_sharpening = np.array([[-1, -1, -1],
 #                                  [-1, 9, -1],
 #                                  [-1, -1, -1]])
 #
 #    # Applying the sharpening kernel to the grayscale image &amp; displaying it.
 #    print("\n\n--- Effects on S&amp;P Noise Image with Probability 0.5 ---\n\n")
 #
 #    # Applying filter on image with salt &amp; pepper noise
 #
 #    sharpened_img = cv2.filter2D(img, -1, kernel_sharpening)
 #    # viewImage(sharpened_img)
 #
 #    kernel_gausian = np.array([[1/16, 1/8, 1/16],
 #                                  [1/8, 1/4, 1/8],
 #                                  [1/16, 1/8, 1/16]])
 #    gaus_img=cv2.filter2D(img, -1, kernel_gausian, borderType=cv2.BORDER_CONSTANT)
 #    # viewImage(gaus_img)
 #
 #
 #
 #
 #
 #        #Гаусов блюр opencv
 #    # blur = cv2.GaussianBlur(img, (5,5), 0)
 #    # viewImage(blur)
 #
 #            # какой то устранитель шума из ореncv
 #    # dst = cv2.fastNlMeansDenoising(img, None, 10, 10, 7, 21)
 #    # viewImage(dst)
 #        # шо це за дич хз прост исправило задник
 #    # se = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
 #    # bg = cv2.morphologyEx(img, cv2.MORPH_DILATE, se)
 #    # out_gray = cv2.divide(img, bg, scale=255)
 #    # out_binary = cv2.threshold(out_gray, 0, 255, cv2.THRESH_OTSU)[1]
 #    #
 #    # cv2.imshow('binary', out_binary)
 #    # cv2.imwrite('binary.png', out_binary)
 #    #
 #    # cv2.imshow('gray', out_gray)
 #    # cv2.imwrite('gray.png', out_gray)
 #
 #        # Фильтр средней точки
 #    # def midpoint(immg):
 #    #     maxf = maximum_filter(img, (3, 3))
 #    #     minf = minimum_filter(img, (3, 3))
 #    #     midpoint = (maxf + minf) / 2
 #    #     viewImage(midpoint)
 #    #
 #    # print("\n\n---Effects on S&amp;P Noise Image with Probability 0.5---\n\n")
 #    # midpoint(img)
 #
 #        # Контрагармонический средний фильтр???????
 #    # def contraharmonic_mean(immg, size, Q):
 #    #     num = np.power(immg, Q + 1)
 #    #     denom = np.power(immg, Q)
 #    #     kernel = np.full(size, 1.0)
 #    #     result = cv2.filter2D(num, -1, kernel) / cv2.filter2D(denom, -1, kernel)
 #    #     return result
 #    #
 #    # print("\n\n--- Effects on S&amp;P Noise Image with Probability 0.5 ---\n\n")
 #    # viewImage(contraharmonic_mean(img, (3, 3), 0.5))
 #
 # # выделение границ и потом их вылавливание
 #    # hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 #    # green_low = np.array([45, 100, 50])
 #    # green_high = np.array([75, 255, 255])
 #    # curr_mask = cv2.inRange(hsv_img, green_low, green_high)
 #    # hsv_img[curr_mask > 0] = ([75, 255, 200])
 #    # viewImage(hsv_img)
 #    # RGB_again = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
 #    # gray = cv2.cvtColor( RGB_again,cv2.COLOR_RGB2GRAY) #RGB_again,
 #    # viewImage(gray)  ## 3
 #    # ret, threshold = cv2.threshold(gray, 90, 255, 0)
 #    # viewImage(threshold)  ## 4
 #    # contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 #    # cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
 #    # viewImage(img)  ## 5

    a=2


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
