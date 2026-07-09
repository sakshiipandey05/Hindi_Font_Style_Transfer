import os
from PIL import Image, ImageDraw, ImageFont

fonts_dir = "../generated_images"
char_code = 2309

images = []
font_names = []

for font_folder in os.listdir(fonts_dir):
    font_path = os.path.join(fonts_dir, font_folder)
    img_path = os.path.join(font_path, f"{char_code}.png")

    if os.path.exists(img_path):
        images.append((Image.open(img_path), font_folder))

width, height = images[0][0].size

result = Image.new("RGB", (width * len(images), height + 40), "white")

draw = ImageDraw.Draw(result)

for i, (img, name) in enumerate(images):
    result.paste(img, (i * width, 0))
    draw.text((i * width + 10, height + 10), name, fill="black")

result.save("../comparison_output.png")

print("Improved comparison created!")
