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

* The input image is preprocessed using OpenCV and ScikitLearn.
* Multiple feature detectors are then applied to the input image to generate corresponding Feature Maps. 
* These Feature Maps form the first Convolutional Layer.
* To this Convolution Layer, rectified linear unit activation function is applied to increase non-linearity in the CNN Model.
* Max Pooling is applied to the convolution layer to get a set of Pooled Feature Maps which makes up the Pooled Layer.
* Multiple such Convolutional and Pooled Layers one after the other are called the hidden layers.
* Flatten function converts the Pooled Feature Maps into numpy vectors that are accepted by ANN.
* The ANN consists of fully connected (dense) hidden layers.
* To deal with Bias-Variance tradeoff, k-fold cross validation is implemented to calculate the variance in accuracy of k trainings.
* Inorder to reduce overfitting, Dropout Regularization is used to randomly deactivate neurons in each hidden layer to reduce dependencies.
* For Hyperparameter Tuning, Grid-Search Cross Validation is used to predict the best set of hyperparameters which lead to max accuracy.
* Because of such a deep classification model, we need to have excellent computational power for training such a deep neural network on a very huge dataset consisting of high resolution images.
* This is where cloud computation will come into the picture which will allow us to do three main things: 1. Store the Dataset on Cloud and import it directly. 2. Train the CNN Model using GPU in the Cloud. 3. Store the resultant h5 files on cloud. 4. Run the prediction algorithms directly onto these stored output h5 files.

## How To Use

1. Download all the python modules as mentioned in the file ‘requirements.pdf’.
2. Open the folder titled ‘Dr.FarmAI’ .
3. Execute the file titled ‘run.py’ using a suitable Python IDE.
4. Once the address of the running localhost port is displayed on the Python
Console, open any suitable browser and browse to that localhost address. Eg.
Running on​ ​http://127.0.0.1:5000/
5. Now you would be directed to the home page of our website.
6. Click on the ‘Register’ tab to create a new account.
7. Click on the ‘Login’ tab and fill all the registered details.
8. After successful login, click on the ‘Start Analysis’ tab.
9. Select any mode of analysis from the two options : Nearby Analysis & Farby
Analysis.
10.Incase of Nearby Analysis, choose a Plant and then upload an image belonging
to any class of that particular plant’s dataset. Click on ‘Predict’ Button to see the
analysis results.
11.Incase of Farby Analysis, choose an image belonging to a particular class from
the Farby dataset and click on ‘Predict’ Button to see the analysis results. 12.Click on the ’Solutions’ tab to seek the solutions for the detected disease.

## Demo

You can [download](https://github.com/amitmerchant1990/electron-markdownify/releases/tag/v1.2.0) the latest installable version of Markdownify for Windows, macOS and Linux.

## License

MIT

