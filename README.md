# Hindi Font Style Transfer

This repository presents the implementation and adaptation of deep learning techniques for Hindi font analysis. It combines two major components:

1. **Hindi Font Classification** using Convolutional Neural Networks (CNN).
2. **Hindi Adaptation of the VQ-Font (ICCV 2023)** framework for Few-Shot Font Generation.

The project began by studying the original VQ-Font implementation, which was developed for **Chinese font generation**, and later adapted its workflow for **Hindi (Devanagari) fonts** by preparing a custom Hindi dataset and preprocessing pipeline.

# Section 1: Hindi Font Classification using CNN

## Objective
- Generate Hindi character images from TrueType (`.ttf`) font files.
- Create a structured Hindi font dataset.
- Train a CNN model to classify different Hindi font styles.
- Predict the font class of unseen Hindi character images.

## Dataset
- **17 Hindi Fonts**
- **43 Hindi Characters**
- **1383 Images**
- **22 Font Classes**

## Workflow
```text
TTF Font Files
      ↓
Character Image Generation
      ↓
Dataset Preparation
      ↓
Train / Validation / Test Split
      ↓
CSV & Excel Metadata Generation
      ↓
CNN Model Training
      ↓
Prediction
      ↓
Model Evaluation
```

## Technologies
- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib
- Scikit-learn

## Outputs
- Training Accuracy Graph
- Training Loss Graph
- Confusion Matrix
- Font Prediction

---
# Section 2: Hindi Adaptation of VQ-Font (Few-Shot Font Generation)

This section is based on the ICCV 2023 paper:

**Few-Shot Font Generation via Transferring Similarity-Guided Global Style and Quantization Local Style**

## Objective
The original VQ-Font framework was designed for **Chinese font generation**. In this work, the framework was studied and adapted for **Hindi (Devanagari) fonts** by replacing the original Chinese dataset with a custom Hindi font dataset. The objective is to generate complete Hindi font styles from only a few reference characters while preserving both global style and local character details.

## Workflow
```text
Chinese VQ-Font Framework
           ↓
Replace Chinese Dataset
           ↓
Prepare Hindi Font Dataset
           ↓
Metadata Generation
           ↓
LMDB Dataset Preparation
           ↓
VQ-Font Training Pipeline
           ↓
Inference
           ↓
Generated Hindi Characters
```
## Work Completed
- Studied the complete VQ-Font architecture and implementation.
- Set up the official repository and installed all required dependencies.
- Explored the dataset preparation and preprocessing pipeline.
- Replaced the original Chinese dataset with a custom Hindi font dataset.
- Generated Hindi character images and metadata for adaptation.
- Prepared the Hindi dataset structure for future VQ-Font training.
- Explored the VQ-VAE-based few-shot font generation pipeline.
- Implemented the Hindi adaptation workflow for future training and inference.

## Technologies
- Python
- PyTorch
- VQ-Font
- OpenCV
- LMDB

---
# Repository Structure
```text
Hindi_Font_Style_Transfer/
│
├── README.md
│
├── Hindi_Adaptation_of_VQFont/
│   ├── Hindi_Adaptation_of_VQFont.ipynb
│   └── README.md
│
├── Hindi_Font_Classification/
│   ├── models/
│   ├── scripts/
│   └── evaluate.py
│
└── Results/
    ├── README.md
    ├── accuracy_graph.png
    ├── comparison_output.png
    ├── confusion_matrix.png
    ├── dataset.xlsx
    └── loss_graph.png
```
---

# Results
The repository includes sample outputs and artifacts generated during the implementation:
- Training Accuracy Graph
- Training Loss Graph
- Confusion Matrix
- Font Comparison Output
- Dataset Metadata (Excel)

---
# Note
To keep the repository lightweight and follow GitHub storage recommendations, the following files are **not included**:
- Generated datasets
- Character images
- Trained model weights (`.keras`)
- Checkpoints
- LMDB databases
- Other large files

---
# References
- **Few-Shot Font Generation via Transferring Similarity-Guided Global Style and Quantization Local Style (ICCV 2023)**
- TensorFlow / Keras Documentation
- PyTorch Documentation
