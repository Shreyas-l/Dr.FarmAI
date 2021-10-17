<!-- <h1 align="center">
	Dr. FarmAI
</h1>

<h3 align="center">Predictive & Prescriptive Analysis of Plant Diseases from Topographical Scans</h3> -->

## Overview

![Intro](https://user-images.githubusercontent.com/58290353/137613411-71a7b671-6e72-4cdd-8ad4-f0cbfd2cbf2c.png)

## Tech Stack

<p align="center">
 <div align="center"><img width="55" src="https://github.com/Shreyas-l/DataSec.AI/blob/main/Documentation/python.png.png"/><img width="55" src="https://github.com/Shreyas-l/DataSec.AI/blob/main/Documentation/docker.png"/><img width="55" src="https://github.com/Shreyas-l/DataSec.AI/blob/main/Documentation/squid.png"/><img width="55" src="https://github.com/Shreyas-l/DataSec.AI/blob/main/Documentation/spacy.png"/><img width="55" src="https://github.com/Shreyas-l/DataSec.AI/blob/main/Documentation/gcp_.png"/><img width="55" src="https://github.com/Shreyas-l/DataSec.AI/blob/main/Documentation/redis.png"/><img width="55" src="https://github.com/Shreyas-l/DataSec.AI/blob/main/Documentation/postgres.png"/><img width="55" src="https://github.com/Shreyas-l/DataSec.AI/blob/main/Documentation/k8_.png"/></div>
</p>

## CNN Implementation

* The input image will first be preprocessed using OpenCV and ScikitLearn Python Libraries.
* We will then be applying multiple feature detectors to the input image inorder to generate multiple Feature Maps. 
* These Feature Maps would form the first Convolutional Layer.
* To this Convolution Layer, we will be applying Rectified Linear Unit Function to increase Non-Linearity in our CNN Model to reduce overfitting.
* We will then be applying Max Pooling to this convolution layer to get a set of Pooled Feature Maps which would make up the Pooled Layer.
* Then there would be multiple such Convolutional and Pooled Layers one after the other as hidden layers.
* We will then apply the Flatten Function to convert the Pooled Feature Maps into numpy vectors that can be accepted by ANN.
* These will then act as the input layer of the ANN model which would consist of fully connected hidden layers.
* To deal with Bias-Variance tradeoff, we will implement k-fold cross validation to get the variance in the accuracy scores of k number of trainings.
* Inorder to reduce overfitting, we will use Dropout Regularization to randomly deactivate neurons in each hidden layer to reduce inter layer over dependencies.
* For Hyperparameter Tuning, we will use Grid-Search Cross Validation to predict the best set of hyperparameters which lead to max accuracy.
* Because of such a deep classification model, we need to have excellent computational power for training such a deep neural network on a very huge dataset consisting of high resolution images.
* This is where cloud computation will come into the picture which will allow us to do three main things: 1. Store the Dataset on Cloud and import it directly. 2. Train the CNN Model using GPU in the Cloud. 3. Store the resultant h5 files on cloud. 4. Run the prediction algorithms directly onto these stored output h5 files.

## How To Use


## Demo

You can [download](https://github.com/amitmerchant1990/electron-markdownify/releases/tag/v1.2.0) the latest installable version of Markdownify for Windows, macOS and Linux.

## License

MIT

