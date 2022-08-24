import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def histogram(img,bins):
  hist = np.zeros(bins)
  for i in range(len(img)):
    hist[img[i]]+=1
  return hist

def cumsum(hist):
  sum = [hist[0]]
  for i in range(1,len(hist)):
    sum.append(sum[-1]+hist[i])
  sum = np.array(sum)

  # normalisation
  sum = (sum - sum.min())/(sum.max() - sum.min())
  sum *= 255
  return sum

def my_equalizing_histograms(src):
  """
  :param src: input image
  :rtype: image 
  :return dest: histogram equalized src image
  """
  dest = None
  # [TODO] 
  img = np.asarray(src)
  img_flat = img.flatten()
  h = histogram(img_flat,256)
  c = cumsum(h).astype('uint8')
  dest = c[img_flat]
  dest = np.reshape(dest, img.shape)
  return dest