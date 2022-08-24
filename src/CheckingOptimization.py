from utils.utils import load_image
from myHistEqualization import my_equalizing_histograms
from myHistMatching import my_matching_histograms
import cv2
from inBuiltEqualization import gray
from skimage import exposure
import timeit
src = load_image(1)
dst = load_image(2)

def giveTime(testcode):
    import_module = "import random"
    print(timeit.repeat(stmt=testcode, setup=import_module))
    
testcode = ''' 
    my_equalizing_histograms(src)
    my_matching_histograms(src,dst)
    '''
giveTime(testcode)

testcode = '''
    equalized_gray = cv2.equalizeHist(gray)
    '''

giveTime(testcode)

testcode = '''
    my_equalizing_histograms(src)
    '''

giveTime(testcode)
testcode = '''
    matched_src = exposure.match_histograms(src,dst)
    '''

giveTime(testcode)

testcode = '''
    my_matching_histograms(src,dst)
    '''
giveTime(testcode)
