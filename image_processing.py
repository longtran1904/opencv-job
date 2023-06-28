from __future__ import print_function
import cv2 as cv
import os
import numpy as np
import random as rng


mounted_directory = '/container_directory'  # Replace with the actual container directory path
local_directory = './images'
processed_directory = './processed'

# Create processed image folder if not exists
if not os.path.exists(processed_directory):
    os.mkdir(processed_directory)


# Process each file in the mounted directory
count = 0
for filename in os.listdir(local_directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(local_directory, filename)
        src = cv.imread(image_path) # src image

        src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        src_gray = cv.blur(src_gray, (3,3))
        ###
        # Perform image processing operations using OpenCV
        ###
        threshold = 100

        # Detect edges using Canny
        canny_output = cv.Canny(src_gray, threshold, threshold * 2)

        # Find contours
        contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Find the convex hull object for each contour
        hull_list = []
        for i in range(len(contours)):
            hull = cv.convexHull(contours[i])
            hull_list.append(hull)

        # Draw contours + hull results
        drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
        for i in range(len(contours)):
            color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
            cv.drawContours(drawing, contours, i, color)
            cv.drawContours(drawing, hull_list, i, color)

        # Save the processed image
        processed_image_path = os.path.join(processed_directory, 'processed_' + filename)
        cv.imwrite(processed_image_path, drawing)

        print(f"Processed {filename} and saved as processed_{filename}")
        count += 1

print(f"processed {count} images")
