from PIL import Image, ImageFilter
import cv2
import numpy as np

def convert_to_grayscale(image_path, output_path="grayscale.jpg"):
    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_path)
    print(f"Grayscale image saved as {output_path}")

def apply_blur(image_path, output_path="blurred.jpg", radius=5):
    image = Image.open(image_path)
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
    blurred_image.save(output_path)
    print(f"Blurred image saved as {output_path}")

def detect_edges(image_path, output_path="edges.jpg", threshold1=100, threshold2=200):
    image = Image.open(image_path).convert("L")
    image_cv = np.array(image)
    edges = cv2.Canny(image_cv, threshold1, threshold2)
    cv2.imwrite(output_path, edges)
    print(f"Edge-detected image saved as {output_path}")

def shrink_image(image_path, output_path="shrunk.jpg", scale_factor=0.5):
    image = Image.open(image_path)
    new_size = (int(image.width * scale_factor), int(image.height * scale_factor))
    
    shrunk_image = image.resize(new_size)
    shrunk_image.save(output_path)
    print(f"Shrunk image saved as {output_path}")

image_path = "Activity 8\logo.jpg"

convert_to_grayscale(image_path)
apply_blur(image_path)
detect_edges(image_path)
shrink_image(image_path)