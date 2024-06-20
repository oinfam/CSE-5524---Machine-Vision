from skimage import io, color, util
import numpy as np
import os

# Problem 1
file = os.getcwd() + '/HW1/buckeyes_gray.bmp'
grayImg = io.imread(file)
io.imshow(grayImg)
io.show()
io.imsave('grayImg.jpeg', grayImg)

file = os.getcwd() + '/HW1/buckeyes_rgb.bmp'
rgbImg = io.imread(file)
io.imshow(rgbImg)
io.show()
io.imsave('rgbImg.jpeg', rgbImg)

# Problem 2
converted = color.rgb2gray(rgbImg)
io.imshow(converted)
io.show()
converted = util.img_as_uint(converted)
io.imsave('converted.png', converted)

# Problem 3
black = np.zeros((10, 10))
white = 255*np.ones((10, 10))
pattern = np.hstack((black, white))
pattern = np.vstack((pattern, np.fliplr(pattern)))
checker = np.tile(pattern, (5, 5))
checker = checker.astype(np.uint8)
io.imsave('checker.jpeg', checker)
io.imshow(checker, cmap='gray')
io.show()


