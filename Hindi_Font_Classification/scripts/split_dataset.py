import os
import random
import shutil

input_dir = "../generated_images"
output_dir = "../dataset_split"

os.makedirs(output_dir, exist_ok=True)

train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

for font_folder in os.listdir(input_dir):
    font_path = os.path.join(input_dir, font_folder)

    if not os.path.isdir(font_path):
        continue

    images = os.listdir(font_path)
    random.shuffle(images)

    train_cut = int(len(images) * train_ratio)
    val_cut = int(len(images) * (train_ratio + val_ratio))

    splits = {
        "train": images[:train_cut],
        "val": images[train_cut:val_cut],
        "test": images[val_cut:]
    }

    for split in splits:
        split_folder = os.path.join(output_dir, split, font_folder)
        os.makedirs(split_folder, exist_ok=True)

        for img in splits[split]:
            src = os.path.join(font_path, img)
            dst = os.path.join(split_folder, img)
            shutil.copy(src, dst)

print("Dataset split done!")
