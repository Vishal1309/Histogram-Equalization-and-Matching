from myHistEqualization import my_equalizing_histograms
from utils.utils import calculate_hist
from inBuiltEqualization import gray, equalized_gray

c = my_equalizing_histograms(gray)
print("Original Image")
calculate_hist(gray)
print("My Equalization Image")
my_equalization = calculate_hist(c)
print("Inbuilt Equalization Image")
inbuilt_equalization = calculate_hist(equalized_gray)
if my_equalization==inbuilt_equalization:
  print("My function is same as inbuilt")
else:
  print("Not Equal")