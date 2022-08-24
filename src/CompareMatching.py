from myHistMatching import my_matching_histograms
from inBuiltMatching import src, dst, matched_src
from utils.utils import compare_matched_hist
matched = my_matching_histograms(src, dst)

compare_matched_hist(src,dst,matched)

if matched_src.all()==matched.all():
    print("Equal")
else:
    print("not")