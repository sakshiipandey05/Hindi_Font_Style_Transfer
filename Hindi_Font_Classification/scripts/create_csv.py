import os
import csv

# ===========================
# Project Paths
# ===========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_DIR = os.path.join(BASE_DIR, "dataset_split")
OUTPUT_CSV = os.path.join(BASE_DIR, "dataset.csv")

total_images = 0


# ===========================
# Unicode filename -> Character
# ===========================

def get_character(filename):
    try:
        unicode_value = int(os.path.splitext(filename)[0])
        return chr(unicode_value)
    except:
        return "Unknown"


# ===========================
# Create CSV
# ===========================

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "Image Name",
        "Character",
        "Font Name",
        "Split"
    ])

    # train / val / test
    for split in ["train", "val", "test"]:

        split_path = os.path.join(DATASET_DIR, split)

        if not os.path.exists(split_path):
            continue

        for font_name in sorted(os.listdir(split_path)):

            font_path = os.path.join(split_path, font_name)

            if not os.path.isdir(font_path):
                continue

            images = sorted(os.listdir(font_path))

            for filename in images:

                if not filename.lower().endswith(".png"):
                    continue

                character = get_character(filename)

                writer.writerow([
                    filename,
                    character,
                    font_name,
                    split
                ])

                total_images += 1


print("CSV created successfully!")
print("Saved at:", OUTPUT_CSV)
print("Total Images:", total_images)
