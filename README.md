# WisconsinAutonomousCodingChallenge

**Final Answer**
![](https://github.com/Warel123-R/WisconsinAutonomousCodingChallenge/blob/95f258dcdc5220572e7b2d328b0fb4d0ad6b0962/answer.png)

**Methodology**
At first I tried working with grayscale but this didn't work because I needed to work with the saturation of the code to filter the cones and to be able to draw the line through them. Then, I started working more with the hsv filter and contours, which gets the bounding boxes of the cones. This allowed me to use linear regression to draw the line through the cones.

**What I tried / Why it didn't work**
At first I tried working with grayscale but this didn't work because I needed to work with the saturation of the code to filter the cones and to be able to draw the line through them. Then, I ran into issues with the lines being completely innacurate due to the hsv thresholds being innacurate and the mask not working properly. So, I started experimenting with different values for the hsv threshold and eventually created an effective mask. Finally, I started working with contours, which gets the bounding boxes of the cones. This allowed me to use linear regression to draw the line through the cones.

**Libraries**
The libraries I used are OpenCV and NumPy
