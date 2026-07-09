import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load model
model = tf.keras.models.load_model("models/font_classifier.keras")
print("Model loaded successfully")

# Test directory
test_dir = "dataset_split/test"

# AUTO CLASS ORDER (VERY IMPORTANT)
class_names = sorted(os.listdir(test_dir))
print("Classes:", class_names)

y_true = []
y_pred = []

for class_name in class_names:
    folder = os.path.join(test_dir, class_name)
    print("Processing:", class_name)

    for img_name in os.listdir(folder):
        img_path = os.path.join(folder, img_name)

        img = image.load_img(img_path, target_size=(128, 128))
        img = image.img_to_array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        pred = model.predict(img, verbose=0)

        pred_index = np.argmax(pred)
        pred_class = class_names[pred_index]

        y_true.append(class_name)
        y_pred.append(pred_class)

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)
sns.heatmap(cm, annot=False, xticklabels=class_names, yticklabels=class_names, cmap="Blues")
plt.close('all')  
plt.figure(figsize=(4,4))

sns.heatmap(
    cm,
    annot=False,
    xticklabels=class_names,
    yticklabels=class_names,
    cmap="Blues"
)

plt.xticks(rotation=45, ha='right', fontsize=7)
plt.yticks(fontsize=7)

plt.tight_layout()
plt.show()
print(classification_report(y_true, y_pred))
