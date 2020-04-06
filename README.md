# Semantic Segmentation
Semantic segmentation is a computer vision technique that enables computers to discern one region in an image from another, based on the semantic context of that region. Semantic segmentation has many applications in diverse fields like medicine, Autonomous driving., and agriculture.
# Dataset
The dataset used for Semantic Segmentation is  Monuseg dataset which contains multi organ tissue images with the ground truth segmentation masks. The dataset used for training the and testing the model can be downloaded from this [link](https://drive.google.com/open?id=1LEn2IXZkxLPRUd2ydbL_ZvXR5Yw5PE64). of google drive and information about dataset is available on this [link](https://monuseg.grand-challenge.org/Data/).

# Models
The following three models have been trained.  
# 1.UNET
![UNET](Images/UNET.PNG)
# 2.SEGNET
![SEGNET](Images/SEGNET.PNG)
# 3.Deep Lab V3 Plus
![DeepLabv3Plus](Images/DeepLabV3Plus.PNG)
![DeepLabv3+](Images/DeepLabV3+.PNG)
# Quantitative Results
The results are shown below
   # Training
| Model | Loss | Accuracy | F1 Score | Dice Score |
| ----- | ---- | ---- | ---- | ---- |
| UNET | 0.0869 | 0.9633 | 0.9328 | 0.9848 
| SEGNET | 0.2399 | 0.8965 | 0.8085 | 0.9572 
| DeepLabV3Plus | 0.0455 | 0.9806 | 0.9645 | 0.9919
  # Validation
| Model | Loss | Accuracy | F1 Score | Dice Score |
| ----- | ---- | ---- | ---- | ---- |
| UNET | 0.1100 | 0.9555 | 0.9216 | 0.9809 
| SEGNET | 0.2431 | 0.8946 | 0.8090 | 0.9560 
| DeepLabV3Plus | 0.1035 | 0.9635 | 0.9347 | 0.9847

 # Testing 
| Model | Loss | Accuracy | F1 Score | Dice Score |
| ----- | ---- | ---- | ---- | ---- |
| UNET | 0.2981 | 0.9054 | 0.7715 | 0.9587 
| SEGNET | 0.2250 | 0.9028 | 0.9581 | 0.7663 
| DeepLabV3Plus | 0.2250 | 0.9028 | 0.9581 | 0.7663

# Qualitative Results
Some predicted results are shown below and graphs and other results can be seen on this  [link](https://github.com/arslanamin14/Image-Segmentation/tree/master/Results)
# 1.UNET
![test1](https://github.com/arslanamin14/Image-Segmentation/blob/master/Results/UNET/Testing%20Image%20With%20Ground%20Truth%20and%20Predicted.PNG)
# 2.SEGNET
![test2](https://github.com/arslanamin14/Image-Segmentation/blob/master/Results/SEGNET/Testing%20Image%20With%20Ground%20Truth%20and%20Predicted.PNG)
# 3.Deep Lab V3 Plus
![test3](https://github.com/arslanamin14/Image-Segmentation/blob/master/Results/DeepLabV3plus/Testing%20Image%20With%20Ground%20Truth%20and%20Predicted.PNG)

# Folder Structure
├── _Code_     
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── UNET.ipynb  
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Segnet.ipynb    
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── DeepLabv3plus.ipynb    
├── _Model_    
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── model-unet.h5  
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── model-Segnet.h5    
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── model-deeplabv3plus.h5
