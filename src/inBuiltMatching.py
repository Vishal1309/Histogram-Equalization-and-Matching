from skimage import exposure
from utils.utils import load_image, compare_matched_hist
src = load_image(3)
dst = load_image(4)
matched_src = exposure.match_histograms(src,dst)

compare_matched_hist(src,dst,matched_src)