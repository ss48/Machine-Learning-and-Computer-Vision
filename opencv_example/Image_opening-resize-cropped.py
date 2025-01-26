from PIL import Image, ImageDraw, ImageFont

# Open the original image
filename = "buildings.jpg" # Path to your image file
with Image.open(filename) as img:
    img.load()

# Set dimensions for cropping
crop_box = (300, 150, 700, 1000)  # (left, upper, right, lower)
cropped_img = img.crop(crop_box)

# Draw annotations on a copy of the original image
annotated_img = img.copy()
draw = ImageDraw.Draw(annotated_img)

# Add rectangle to indicate cropping
draw.rectangle(crop_box, outline="red", width=4)

# Function to draw dashed lines
def draw_dashed_line(draw, start, end, dash_length=10, gap_length=5, color="black", width=2):
    x1, y1 = start
    x2, y2 = end
    total_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    num_dashes = int(total_length // (dash_length + gap_length))
    for i in range(num_dashes):
        dash_start = (
            x1 + i * (dash_length + gap_length) * (x2 - x1) / total_length,
            y1 + i * (dash_length + gap_length) * (y2 - y1) / total_length,
        )
        dash_end = (
            dash_start[0] + dash_length * (x2 - x1) / total_length,
            dash_start[1] + dash_length * (y2 - y1) / total_length,
        )
        draw.line([dash_start, dash_end], fill=color, width=width)

# Draw dashed lines for crop boundaries
draw_dashed_line(draw, (300, 0), (300, 150), color="red", width=2)  # Left vertical
draw_dashed_line(draw, (700, 0), (700, 150), color="red", width=2)  # Right vertical
draw_dashed_line(draw, (300, 1000), (300, annotated_img.height), color="red", width=2)  # Left bottom
draw_dashed_line(draw, (700, 1000), (700, annotated_img.height), color="red", width=2)  # Right bottom
draw_dashed_line(draw, (0, 150), (300, 150), color="red", width=2)  # Top horizontal
draw_dashed_line(draw, (700, 150), (annotated_img.width, 150), color="red", width=2)  # Top horizontal
low_res_img = cropped_img.reduce(4)
# Add dimension labels
font_size = 24  # Adjust as needed
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

draw.text((310, 50), "150", fill="black", font=font)  # Vertical dimension
draw.text((310, 1020), "1000", fill="black", font=font)  # Bottom vertical
draw.text((200, 170), "300", fill="black", font=font)  # Horizontal left
draw.text((720, 170), "700", fill="black", font=font)  # Horizontal right

# Show or save the annotated image
annotated_img.show()  # Opens the image with annotations
low_res_img.show()
cropped_img.show()
annotated_img.save("annotated_image.png")
cropped_img.save("cropped_image.png")
low_res_img.save("low_resolution_image.png")

filename = "low_resolution_image.png" # Path to your image file
with Image.open(filename) as img_low_res:
    img_low_res.load()
img_low_res.format
print("img-format:" , img.format)

img_low_res.size
print("img-size:" , img_low_res.size)

img_low_res.mode
print("img-mode:", img_low_res.mode)