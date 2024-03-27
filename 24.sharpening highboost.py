import cv2
import numpy as np

image_path = r"C:\Users\hp\OneDrive\Pictures\Saved Pictures\bike.jpeg"
original_img = cv2.imread(image_path)

gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

high_freq_img = gray_img - blurred_img

alpha = 1.5

sharpened_img = cv2.addWeighted(gray_img, 1 + alpha, high_freq_img, -alpha, 0)
