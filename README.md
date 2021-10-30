<!-- <h1 align="center">
	Dr. FarmAI
</h1>

<h3 align="center">Predictive & Prescriptive Analysis of Plant Diseases from Topographical Scans</h3> -->

<h1 align="center">
  <br>
  <img src="https://github.com/Shreyas-l/AmWell/blob/main/Documentation/AmWell.png" alt="Markdownify" width="200">
  <br>
  Dr. FarmAI - Predictive & Prescriptive Analysis of Plant Diseases from Topographical Scans
  <br>
</h1>

<h3 align="center">TechStack</h3>

<p align="center">

<div align="center"><img width="55" src="https://raw.githubusercontent.com/gilbarbara/logos/master/logos/angular-icon.svg"/><img width="55" src="https://raw.githubusercontent.com/gilbarbara/logos/master/logos/bootstrap.svg"/><img width="55" src="https://raw.githubusercontent.com/gilbarbara/logos/master/logos/eslint.svg"/><img width="55" src="https://raw.githubusercontent.com/gilbarbara/logos/master/logos/jasmine.svg"/><img width="55" src="https://raw.githubusercontent.com/gilbarbara/logos/master/logos/javascript.svg"/><img width="55" src="https://raw.githubusercontent.com/gilbarbara/logos/master/logos/karma.svg"/><img width="55" src="https://raw.githubusercontent.com/gilbarbara/logos/master/logos/protactor.svg"/><img width="55" src="https://raw.githubusercontent.com/gilbarbara/logos/master/logos/typescript-icon.svg"/></div>
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#demo">Demonstration</a> •
  <a href="#cnn">CNN Implementation</a> •
  <a href="#demo">Demonstration</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#pub">Research Publication</a>
</p>

<div id="overview"></div>

## Overview

![Intro](https://user-images.githubusercontent.com/58290353/137613411-71a7b671-6e72-4cdd-8ad4-f0cbfd2cbf2c.png)

<div id="demo"></div>

## Demonstration

https://user-images.githubusercontent.com/58290353/137632130-cc62138d-8061-4b29-b6d1-67910a116ad6.mp4

<div id="cnn"></div>

## CNN Implementation

* The input image is preprocessed using OpenCV and ScikitLearn.
* Multiple feature detectors are then applied to the input image to generate corresponding Feature Maps. 
* These Feature Maps form the first Convolutional Layer.
* To this Convolution Layer, rectified linear unit activation is applied to increase non-linearity in the CNN Model.
* Max Pooling is applied to convolution layer to get a set of Pooled Feature Maps which makes up Pooled Layer.
* Multiple such Convolutional and Pooled Layers one after the other are called the hidden layers.
* Flatten function converts the Pooled Feature Maps into numpy vectors that are accepted by ANN.
* The ANN consists of fully connected (dense) hidden layers.
* For Bias-Variance tradeoff, k-fold cross validation is implemented (variance in accuracy of k trainings).
* To reduce overfitting, Dropout Regularization is used to randomly deactivate neurons & reduce dependencies.
* For Hyperparameter Tuning, Grid-Search Cross Validation is used to predict the best set of hyperparameters.
* Because of the deep CNN, we need to have excellent computational power for training on a huge dataset.
* This is where cloud computation on Kaggle leveraging GPU comes into the picture.

<div id="how-to-use"></div>

## How To Use

1. Download all the python modules as mentioned in the file ‘requirements.pdf’.
1. Open the folder titled ‘Dr.FarmAI’ .
1. Execute the file titled ‘run.py’ using a suitable Python IDE.
1. Once the address of the running localhost port is displayed on the Python Console, open any suitable browser and browse to that localhost address. Eg. Running on​ ​http://127.0.0.1:5000/
1. Now you would be directed to the home page of our website.
1. Click on the ‘Register’ tab to create a new account.
1. Click on the ‘Login’ tab and fill all the registered details.
1. After successful login, click on the ‘Start Analysis’ tab.
1. Select any mode of analysis from the two options - Nearby Analysis & Farby Analysis.
1. Incase of Nearby Analysis, choose a Plant and then upload an image belonging to any class of that particular plant’s dataset. 
1. Click on ‘Predict’ Button to see the analysis results.
1. Incase of Farby Analysis, choose an image belonging to a particular class from the Farby dataset and click on ‘Predict’ Button to see the analysis results.
1. Click on the ’Solutions’ tab to seek the solutions for the detected disease.

<div id="pub"></div>

## Research Publication

### [Performance Analysis of Optimizers for Plant Disease Classification with Convolutional Neural Networks](https://ieeexplore.ieee.org/document/9487698)

<p>Crop failure owing to pests & diseases are inherent within Indian agriculture, leading to annual losses of 15-25% of productivity, resulting in a huge economic loss. This research analyzes the performance of various optimizers for predictive analysis of plant diseases with a deep learning approach. The research uses Convolutional Neural Networks for the classification of farm/plant leaf samples of 3 crops into 15 classes. The various optimizers used in this research include RMSprop, Adam, and AMSgrad. Optimizers' Performance is visualized by plotting the Training and Validation Accuracy and Loss curves, ROC curves, and Confusion Matrix. The best performance is achieved using Adam optimizer, with the maximum validation accuracy being 98%. This paper focuses on the research analysis proving that plant diseases can be predicted and pre-empted using deep learning methodology with the help of satellite, drone-based or mobile-based images that result in reducing crop failure and agricultural losses.
</p> 


## License

MIT

