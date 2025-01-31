from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "image.jpg"  # Replace with your image path
image = Image.open(image_path)

# Convert to Grayscale
grayscale = image.convert("L")

# Apply Gaussian Blur with a defined filter size (Kernel: 5x5)
gaussian_blur = image.filter(ImageFilter.GaussianBlur(radius=5))

# Apply Edge Detection using a kernel
edges = image.filter(ImageFilter.FIND_EDGES)

# Define a sharpening kernel
sharpening_kernel = ImageFilter.Kernel(
    size=(3, 3),  # 3x3 filter
    kernel=[0, -1, 0, -1, 5, -1, 0, -1, 0],  # Sharpening matrix
    scale=None
)
sharpened = image.filter(sharpening_kernel)

# Store images and labels
filtered_images = [image, grayscale, gaussian_blur, edges, sharpened]
labels = ["Original", "Grayscale", "Gaussian Blur (5x5)", "Edge Detection", "Sharpened (3x3)"]

# Function to add labels to images
def add_label(img, text):
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()  # Default font
    draw.text((10, 10), text, fill="red", font=font)  # Position and text colour
    return img

# Apply labels to images
labeled_images = [add_label(img.copy(), label) for img, label in zip(filtered_images, labels)]

# Create a subplot layout
fig, axes = plt.subplots(1, 5, figsize=(15, 5))

# Display images with labels
for ax, img in zip(axes, labeled_images):
    ax.imshow(img, cmap="gray" if img.mode == "L" else None)  # Handle grayscale properly
    ax.axis("off")  # Hide axes

# Show the images
plt.tight_layout()
plt.show()
