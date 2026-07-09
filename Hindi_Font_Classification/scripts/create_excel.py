import os
from openpyxl import Workbook

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_DIR = os.path.join(BASE_DIR, "dataset_split")
OUTPUT_FILE = os.path.join(BASE_DIR, "dataset.xlsx")

# Unicode filename -> Hindi Character
char_map = {
    "2309": "अ",
    "2310": "आ",
    "2311": "इ",
    "2312": "ई",
    "2313": "उ",
    "2314": "ऊ",
    "2319": "ए",
    "2320": "ऐ",
    "2323": "ओ",
    "2324": "औ",
    "2325": "क",
    "2326": "ख",
    "2327": "ग",
    "2328": "घ",
    "2329": "ङ",
    "2330": "च",
    "2331": "छ",
    "2332": "ज",
    "2333": "झ",
    "2334": "ञ",
    "2335": "ट",
    "2336": "ठ",
    "2337": "ड",
    "2338": "ढ",
    "2339": "ण",
    "2340": "त",
    "2341": "थ",
    "2342": "द",
    "2343": "ध",
    "2344": "न",
    "2346": "प",
    "2347": "फ",
    "2348": "ब",
    "2349": "भ",
    "2350": "म",
    "2351": "य",
    "2352": "र",
    "2354": "ल",
    "2357": "व",
    "2358": "श",
    "2359": "ष",
    "2360": "स",
    "2361": "ह"
}

wb = Workbook()
ws = wb.active
ws.title = "Dataset"

ws.append(["Image Name", "Character", "Font Name", "Split"])

count = 0

for split in ["train", "val", "test"]:

    split_path = os.path.join(DATASET_DIR, split)

    if not os.path.exists(split_path):
        continue

    for font in sorted(os.listdir(split_path)):

        font_path = os.path.join(split_path, font)

        if not os.path.isdir(font_path):
            continue

        for img in sorted(os.listdir(font_path)):

            if img.endswith(".png"):

                code = os.path.splitext(img)[0]

                character = char_map.get(code, "Unknown")

                ws.append([
                    img,
                    character,
                    font,
                    split
                ])

                count += 1

# Auto width
for column in ws.columns:
    max_len = max(len(str(cell.value)) if cell.value else 0 for cell in column)
    ws.column_dimensions[column[0].column_letter].width = max_len + 5

wb.save(OUTPUT_FILE)

print("Excel created successfully!")
print("Saved at:", OUTPUT_FILE)
print("Total Images:", count)
