from PIL import Image

filename = "strawberry.jpg"
with Image.open(filename) as img:
    img.load()

# Check image mode
print("Image mode:", img.mode)

# Convert to CMYK and Grayscale
cmyk_img = img.convert("CMYK")
gray_img = img.convert("L")  # Grayscale

cmyk_img.show()
gray_img.show()

# Check the bands of each image
print("RGB bands:", img.getbands())  # Should output ('R', 'G', 'B', 'A') for RGBA
print("CMYK bands:", cmyk_img.getbands())  # ('C', 'M', 'Y', 'K')
print("Grayscale bands:", gray_img.getbands())  # ('L',)
#red, green, blue, alpha = img.split() is used to unpack all four channels since the image is in RGBA mode.
#If the alpha channel is not needed, you can ignore it with _ like this: red, green, blue, _ = img.split().
# Split the RGBA image into individual bands
#Red channel: (red, zeroed_band, zeroed_band)
#Green channel: (zeroed_band, green, zeroed_band)
#Blue channel: (zeroed_band, zeroed_band, blue)
red, green, blue, alpha = img.split()

# Create a zeroed-out band
zeroed_band = red.point(lambda _: 0)

# Merge bands to isolate red, green, and blue
red_merge = Image.merge(
    "RGB", (red, zeroed_band, zeroed_band)
)

green_merge = Image.merge(
    "RGB", (zeroed_band, green, zeroed_band)
)

blue_merge = Image.merge(
    "RGB", (zeroed_band, zeroed_band, blue)
)

# Display the resulting images
#red_merge.show()
#green_merge.show()
#blue_merge.show()
width, height = red_merge.size

# Create a blank canvas to hold the three images side by side
#Blank Canvas: A new blank canvas is created using Image.new() with dimensions width * 3 
# by height to hold all three images side by side.

#Pasting Images:canvas.paste() is used to paste each image (red_merge, green_merge, blue_merge) 
# onto the canvas at specific positions: (0, 0), (width, 0), and (width * 2, 0).
combined_width = width * 3  # Three images side by side
combined_height = height  # Height remains the same
canvas = Image.new("RGB", (combined_width, combined_height))

# Paste the images onto the canvas
canvas.paste(red_merge, (0, 0))  # Place the red image on the left
canvas.paste(green_merge, (width, 0))  # Place the green image in the middle
canvas.paste(blue_merge, (width * 2, 0))  # Place the blue image on the right

# Show the combined image
canvas.show()

# Optionally save the combined image
canvas.save("combined_rgb_channels.jpg")
combined_width = width  # Width remains the same
combined_height = height * 3  # Three images stacked vertically
canvas = Image.new("RGB", (combined_width, combined_height))

canvas.paste(red_merge, (0, 0))  # Place the red image at the top
canvas.paste(green_merge, (0, height))  # Place the green image in the middle
canvas.paste(blue_merge, (0, height * 2))  # Place the blue image at the bottom

canvas.show()
