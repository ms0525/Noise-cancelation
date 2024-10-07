# Noise-cancelation
In this project I will be implementing deep learning to reduce the noise from images and audio files.

Image Noise Reduction Using CNN
1 - Introduction
Noise reduction can be implemented on both images and audio files. In this project I will implement it on both types. First we will start working with images as it will gives us an understanding of how Convolutional Neural Network (CNN) works. I will try my best to explain each and every step in deapth.

1.1 - Noise
Noise is any unwanted signal in any signal. In context of images it is random variation of brightness or color information in images, and is usually an aspect of electronic noise (wikipedia: https://en.wikipedia.org/wiki/Image_noise). In audio, noise is unwanted or harmful sound considered unpleasant, loud, or disruptive to hearing (wikipedia: https://en.wikipedia.org/wiki/Noise).

1.2 - Clean image or audio
When noise is reduced or canceled out the outcome we get is clean image or audio.

1.3 - Steps of Training a Neural Network
Following are the steps of training a neural network:

Data preprocessing
Define Model
Forward Propagation
Calculate Loss
Backward Propagation
Update weights
Repeat
Pre-requsite
Neural Network

2 - Image Noise Reduction
We will be using supervised learning. The dataset we need to train the CNN will consist of

Noisy images
Clean images (Actual images)
We will feed the noisy images to CNN and it will predict a clean image (predicted image), then it will compare the clean images, predicted and actual image, and calculates the loss. Then it will update the weights accordingly. This process will repeat until we will get our desired results. This is the general overview of our training. We will discuss each and every step in detail when implementing.

We can use 2 types of dataset to train our model.

1. Dataset contains both noisy and clean images.
2. Dataset is a set of clean images and we add noise to is using python.

we will try it with 2nd approch.

You can use the dataset using the following command:

`
! kaggle datasets download -d balraj98/berkeley-segmentation-dataset-500-bsds500
`

I will be listing all the steps performed in noise_reduction.ipynb

1. Add gaussian noise to the images
2. Split dataset into training, validating and testing dataset
3. Normalizing datasets (range 0 - 1)
4. Creating U-Net CNN model for noise reduction 
5. Train model using model.fit() method for 50 epochs
6. Rescale image
7. Visualize the results 

## Results
![image](https://github.com/user-attachments/assets/f72d6b4d-d615-4af0-8821-3f0f3bbba6b0)
