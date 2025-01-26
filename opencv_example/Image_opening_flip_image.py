from PIL import Image

# Open the original image
filename = "buildings.jpg"
with Image.open(filename) as img:
    img.load()

# Print image properties
print("img-format:", img.format)
print("img-size:", img.size)
print("img-mode:", img.mode)

# Perform image transformations
converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)  # Flip the image top to bottom
converted_img_transpose = img.transpose(Image.TRANSVERSE)  # Apply transverse transformation 270 degree rotation

# Display the transformed images
converted_img.show()  # Flipped image
converted_img_transpose.show()  # Transposed image
img.show()  # Original image
rotated_img = img.rotate(45, expand=True)
rotated_img.show()