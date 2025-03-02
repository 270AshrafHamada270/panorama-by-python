import cv2 
import numpy as np
import os

def load_images_from_folder(folder):
    images = []
    for filename in sorted(os.listdir(folder)):
        img_path = os.path.join(folder, filename)
        img = cv2.imread(img_path)
        if img is not None:
            images.append(img)
    return images

def stitch_images(images):
    # Create a stitcher object (Use cv2.createStitcher() for OpenCV < 4)
    stitcher = cv2.Stitcher_create()
    status, panorama = stitcher.stitch(images)
    
    if status == cv2.Stitcher_OK:
        return panorama
    else:
        print("Error during stitching: ", status)
        return None

# Define the folder path
folder_path = r"F:\Quiz_CV\Images"

# Load images
images = load_images_from_folder(folder_path)

# Check if images are loaded
if len(images) < 2:
    print("Error: Need at least 2 images for stitching")
else:
    # Stitch images
    panorama = stitch_images(images)
    
    if panorama is not None:
        # Show the result
        cv2.imshow("Panorama", panorama)
        cv2.imwrite("panorama_result.jpg", panorama)
        cv2.waitKey(0)
        cv2.destroyAllWindows()