# Hindi_Font_Style_Transfer
Implementation and Hindi adaptation of the ICCV 2023 VQ-Font paper (Few-Shot Font Generation) along with a CNN-based Hindi Font Classification pipeline using Deep Learning and Computer Vision.
This repository contains two related projects. The first focuses on classifying Hindi font styles using a Convolutional Neural Network (CNN), while the second adapts the VQ-Font framework for Hindi Few-Shot Font Generation, enabling the generation of unseen Hindi characters from only a few reference characters.

# Repository Structure
Hindi_Font_Style_Transfer/
│
├── README.md
├── Hindi_Adaptation_of_VQFont/
│   └── Hindi_Adaptation_of_VQFont.ipynb
├── Hindi_Font_Classification/
│   └── Hindi_Font_Classification.ipynb
└── Results/
    ├── accuracy_graph.png
    ├── loss_graph.png
    ├── prediction_output.png
    └── confusion_matrix.png

# Project 1: Hindi Font Classification using CNN

## Objective
- Generate Hindi character images from TTF font files.
- Create a Hindi font dataset.
- Train a CNN model to classify different Hindi font styles.
- Predict the font of unseen images.

## Dataset
- **17 Hindi Fonts**
- **43 Hindi Characters**
- **1383 Images**
- **22 Font Classes**

## Workflow
TTF Fonts → Character Generation → Dataset Split → CSV Metadata → CNN Training → Prediction → Evaluation

## Results
- Accuracy Graph
- Loss Graph
- Prediction Output
- Confusion Matrix

# Project 2: Hindi Adaptation of VQ-Font (Few-Shot Font Generation)

## Objective
Adapt the **VQ-Font (ICCV 2023)** framework for Hindi by reusing the Hindi font dataset created in Project 1. The model learns the writing style from a few reference characters and generates the remaining Hindi characters in the same style.

## Workflow
Hindi Dataset → Metadata Generation → LMDB Conversion → VQ-Font Training → Checkpoint → Inference → Generated Hindi Characters

## Key Features
- Hindi dataset adaptation
- Metadata & Unicode generation
- LMDB dataset creation
- Few-shot font generation
- Inference on Hindi fonts

# Technologies Used

- Python
- TensorFlow
- PyTorch
- CNN
- VQ-Font
- OpenCV
- LMDB
  
# Results

The repository includes:
- Training Accuracy Graph
- Training Loss Graph
- Prediction Output
- Confusion Matrix


# Note

Datasets, generated images, trained model weights, checkpoints, LMDB databases, and other large files are intentionally excluded from this repository.

---

## Author

**Sakshi Pandey**  
B.Tech Information Technology
