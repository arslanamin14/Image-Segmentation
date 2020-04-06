# Semantic Segmentation
Semantic segmentation is a computer vision technique that enables computers to discern one region in an image from another, based on the semantic context of that region. Semantic segmentation has many applications in diverse fields like medicine, Autonomous driving., and agriculture.
# Dataset
The dataset used for Semantic Segmentation is  Monuseg dataset which contains multi organ tissue images with the ground truth segmentation masks. The dataset used for training the and testing the model can be downloaded from this [link](https://drive.google.com/open?id=1LEn2IXZkxLPRUd2ydbL_ZvXR5Yw5PE64). of google drive and information about dataset is available on this [link](https://monuseg.grand-challenge.org/Data/).

# Models
The following three models have been trained.  
1.UNET  
2.SEGNET  
3.DeepLabV3Plus

# UNET

# SEGNET

# Deep Lab V3 Plus

# Quantitative Results
| Model | Loss | Accuracy | F1 Score | Dice Score |
| ----- | ---- | ---- | ---- | ---- |
| Unet | 0.253 | 0.878 | 0.635 | 0.730 
| Segnet | 0.229 | 0.903 | 0.767 | 0.825 
| DeeplabV3+ | 0.102 | 0.962 | 0.917 | 0.932

# Folder Structure
├── _Code_     
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── UNET.ipynb  
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Segnet.ipynb    
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── DeepLabv3plus.ipynb    
├── _Model_    
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── model-unet.h5  
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── model-Segnet.h5    
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── model-deeplabv3plus.h5
