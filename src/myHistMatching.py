import numpy as np
from myHistEqualization import cumsum, histogram

def find(arr, x):
    id = np.abs(arr-x).argmin()
    return id

def my_matching_histograms(src,dst):
  """
  :param src: input image
  :param dst: reference image
  :rtype: image 
  :return mathced_src: histogram matched src image
  """
  matched_src = None
  # [TODO] 
  img_shape = src.shape
  src_flat = src.flatten()
  dst_flat = dst.flatten()
  src_hist = histogram(src_flat,256)
  dst_hist = histogram(dst_flat,256)
  src_cs = cumsum(src_hist)
  dst_cs = cumsum(dst_hist)

  t = []

  for i in range(len(src_hist)):
    id = find(dst_cs, src_cs[i])
    t.append(id)
  matched_src = src_flat
  for i in range(len(matched_src)):
    matched_src[i] = t[matched_src[i]]
  return matched_src.reshape(img_shape)