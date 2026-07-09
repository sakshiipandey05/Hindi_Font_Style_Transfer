import tensorflow as tf
import numpy as np
import os

# -----------------------------
# BASE PATH FIX (IMPORTANT)
# -----------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# -----------------------------
# LOAD MODEL
# -----------------------------
model = tf.keras.models.load_model(
    os.path.join(BASE_DIR, "models/font_classifier.keras")
)

# -----------------------------
# CLASS NAMES (SAME ORDER AS TRAINING)
# -----------------------------
train_path = os.path.join(BASE_DIR, "dataset_split", "train")
class_names = sorted(os.listdir(train_path))

print("Classes:", class_names)
print("Total classes:", len(class_names))

# -----------------------------
# IMAGE PATH (CHANGE ANY IMAGE HERE)
# -----------------------------
img_path = os.path.join(
    BASE_DIR,
    "dataset_split",
    "test",
     "Mukta-Bold",
    "2354.png"
)


# -----------------------------
# LOAD IMAGE
# -----------------------------
img = tf.keras.utils.load_img(img_path, target_size=(128,128))
img_array = tf.keras.utils.img_to_array(img)
img_array = img_array / 255.0

img_array = np.expand_dims(img_array, axis=0)

# -----------------------------
# PREDICT
# -----------------------------
pred = model.predict(img_array)

pred_class = class_names[np.argmax(pred[0])]
confidence = np.max(pred[0]) * 100

actual_font = os.path.basename(os.path.dirname(img_path))

print("\n====================")
print("Actual Font    :", actual_font)
print("Predicted Font :", pred_class)
print("Confidence     :", round(confidence, 2), "%")
print("====================")
