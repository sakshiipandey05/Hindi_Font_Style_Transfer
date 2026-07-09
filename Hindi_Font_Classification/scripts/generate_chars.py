from PIL import Image, ImageDraw, ImageFont
import os

print("Script Started")

FONT_DIR = "../fonts"
OUTPUT_DIR = "../generated_images"

# Debug: check fonts folder content
print("Fonts folder contents:", os.listdir(FONT_DIR))

chars = [
    "अ","आ","इ","ई","उ","ऊ","ए","ऐ","ओ","औ",
    "क","ख","ग","घ","ङ","च","छ","ज","झ","ञ",
    "ट","ठ","ड","ढ","ण","त","थ","द","ध","न",
    "प","फ","ब","भ","म","य","र","ल","व",
    "श","ष","स","ह"
]

os.makedirs(OUTPUT_DIR, exist_ok=True)

for font_file in os.listdir(FONT_DIR):

    if font_file.endswith(".ttf") or font_file.endswith(".otf"):

        print("Processing font:", font_file)

        font_name = os.path.splitext(font_file)[0]

        font_output = os.path.join(OUTPUT_DIR, font_name)
        os.makedirs(font_output, exist_ok=True)

        font_path = os.path.join(FONT_DIR, font_file)

        try:
            font = ImageFont.truetype(font_path, 120)

            for ch in chars:
                img = Image.new("RGB", (256, 256), "white")
                draw = ImageDraw.Draw(img)

                draw.text((80, 60), ch, fill="black", font=font)

                img.save(
                    os.path.join(font_output, f"{ord(ch)}.png")
                )

            print(f"Done: {font_name}")

        except Exception as e:
            print(f"Error with {font_name}: {e}")
