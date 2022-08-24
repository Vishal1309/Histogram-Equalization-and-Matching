# Histogram Equilization and Histogram Specification
## To Run
Go to project directory and type run.sh in terminal

### What are Histograms?
- A histogram is a chart that shows frequency distributions. Frequency distribution shows how often each different value in a dataset occurs.
- In this case, histogram shows the intensity distribution in the image.

### Applications of Histograms?
- It is one of the most frequently used method to plot historical data.
- Histograms are generally used to show if the output of the process follows a certain nature(usually to check if outputs are normally distributed)
- Identifying most common outcome of a process.
- Identifying deviations/trends in data points.

## Histogram Equalizing

### What is Histogram Equalization
- It is a computer image processing technique to improve contrast in an image.
- It essentialy spreads out the most frequent pixel density to make it more equalised/uniform.?

### Observation & Comparison
- Observation: We can see that the input image had vary high number of pixels within a certain small range if intensities. After applying the function, the histogram is more uniform.
- Comparison: Our function produces the same output as to that of the inbuit function.

## Histogram Matching

### What is Histogram Matching?
- Histogram Matching is transformation of an image such that its histogram matches the histogram of another image.
- This is done by finding the mapping between pixel intensity of original image and reference image.

Algorithm:
- Make the CDF of both original and reference image.
- See the value of CDF for a particular pixel intensity (P) in original image. Lets call this X.
- Find the pixel intensity (Q) corresponding to closest value to X in CDF of reference image
-  Change the value of pixels in original image with intensity P to intensity Q.

### Observation & Comparison
- Observation: We can see that after appying the matching, the histogram of final image looks a similar to histogram of reference image.
- Comparison: Our function for matching produces exact same results as the inbuilt function

#### references:
https://towardsdatascience.com/histogram-matching-ee3a67b4cbc1 \\
https://medium.com/hackernoon/histogram-equalization-in-python-from-scratch-ebb9c8aa3f23

