from utils.utils import load_image, calculate_hist
import cv2

gray = load_image(3)
calculate_hist(gray)

equalized_gray = cv2.equalizeHist(gray)
calculate_hist(equalized_gray)