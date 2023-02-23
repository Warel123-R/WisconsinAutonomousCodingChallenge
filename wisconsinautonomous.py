import cv2
import numpy as np

# Load the image
img = cv2.imread('red.png')

# Apply Gaussian blur to remove noise
blurred = cv2.GaussianBlur(img, (11, 11), 0)

# Convert to HSV color space
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

# Define the color range for cones
lower_cone = np.array([0, 200, 150])
upper_cone = np.array([200, 255, 255])

# Threshold the image to get binary image with only cones
mask = cv2.inRange(hsv, lower_cone, upper_cone)
cv2.imshow("mask", mask)

# Find contours of cones in binary image
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area and shape
min_area = 100
max_area = 10000
filtered_contours = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > min_area and area < max_area:
        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.03 * perimeter, True)
        if len(approx) == 4:
            filtered_contours.append(cnt)

# Fit a line to the left and right boundaries of the path
left_boundary = np.array([0, img.shape[0]])
right_boundary = np.array([img.shape[1], img.shape[0]])
for cnt in filtered_contours:
    for point in cnt:
        if point[0][0] < img.shape[1] / 2 and point[0][1] < left_boundary[1]:
            left_boundary = point[0]
        elif point[0][0] > img.shape[1] / 2 and point[0][1] < right_boundary[1]:
            right_boundary = point[0]

# Extend the lines to the bottom of the image
left_slope = (left_boundary[1] - img.shape[0]) / (left_boundary[0] - 0.0)
right_slope = (right_boundary[1] - img.shape[0]) / (right_boundary[0] - img.shape[1])
left_y = int(left_slope * (img.shape[1] / 2.0) + left_boundary[1] - left_slope * left_boundary[0])
right_y = int(right_slope * (img.shape[1] / 2.0) + right_boundary[1] - right_slope * right_boundary[0])
left_bottom = np.array([int((img.shape[0] - left_y) / left_slope), img.shape[0]])
right_bottom = np.array([int((img.shape[0] - right_y) / right_slope + img.shape[1]), img.shape[0]])

# Draw boundary lines on the image
cv2.line(img, (left_boundary[0], left_boundary[1]), (0, img.shape[0]), (0, 0, 255), 10)
cv2.line(img, (right_boundary[0], right_boundary[1]), (img.shape[1], img.shape[0]), (0, 0, 255), 10)

# Save the output image
cv2.imwrite('answer.png', img)
