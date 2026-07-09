import tensorflow as tf
import os

# -----------------------------
# DATA PATH
# -----------------------------
train_dir = "dataset_split/train"
val_dir = "dataset_split/val"

img_size = (128, 128)
batch_size = 16

# -----------------------------
# LOAD DATA
# -----------------------------
train_data = tf.keras.utils.image_dataset_from_directory(
    train_dir,
    image_size=img_size,
    batch_size=batch_size
)

val_data = tf.keras.utils.image_dataset_from_directory(
    val_dir,
    image_size=img_size,
    batch_size=batch_size
)

class_names = train_data.class_names
print("Classes:", class_names)
print("Total classes:", len(class_names))

# -----------------------------
# NORMALIZATION
# -----------------------------
normalization_layer = tf.keras.layers.Rescaling(1./255)

train_data = train_data.map(lambda x, y: (normalization_layer(x), y))
val_data = val_data.map(lambda x, y: (normalization_layer(x), y))

# -----------------------------
# DATA PREFETCH
# -----------------------------
train_data = train_data.cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)
val_data = val_data.cache().prefetch(buffer_size=tf.data.AUTOTUNE)

# -----------------------------
# CNN MODEL (IMPROVED)
# -----------------------------
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(len(class_names), activation='softmax')
])

# -----------------------------
# COMPILE
# -----------------------------
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# -----------------------------
# TRAIN
# -----------------------------
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=30
)

# -----------------------------
# SAVE MODEL
# -----------------------------
model.save("models/font_classifier.keras")

print("Training Completed & Model Saved!")
