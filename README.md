# Crop-Dissease-Classificaton-API
### An API designed for identifying different disseases for a specific crop  
Project Dataset link :- https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset
Classes and models link :- https://drive.google.com/drive/folders/1Cy7sGp29612xIcxxAuV8cvToIvpkUpeO?usp=sharing

# Crop Disease Diagnosis API

The Crop Disease Diagnosis API is a tool that allows users to determine whether a leaf from a given crop is suffering from a disease and identify the specific disease if present. The API is built using a deep learning model based on convolutional neural networks (CNNs) implemented with TensorFlow. The backend is developed using Django, providing a user-friendly interface for making requests and receiving diagnoses.

## Features

- Diagnose crop diseases by uploading a leaf image and providing the crop name.
- Utilizes a CNN-based deep learning model trained on diverse datasets of healthy and diseased leaves.
- Supports authentication and user access control with two roles: `dev` and `farmer`.
- Provides a secure and scalable solution for crop disease diagnosis.

## How It Works

1. Users make a POST request to the API, providing the crop name and an image of a leaf.
2. The Django backend preprocesses the image and passes it to the deep learning model.
3. The model predicts whether the leaf is healthy or diseased and identifies the disease if applicable.
4. The API generates a response with the diagnosis result and returns it to the user.

## Authentication and Access Levels

The API supports user authentication and access control. There are two roles:

- `dev`: Developers or administrators who have access to API development and configuration.
- `farmer`: End-users (farmers) who can use the API for crop disease diagnosis.

## Getting Started

1. Clone this repository to your local machine.
2. Set up your development environment, ensuring you have the required dependencies.
3. Configure the Django settings, including authentication settings and database configuration.
4. Train and load the deep learning model using TensorFlow.
5. Run the Django development server to host the API locally.

## API Usage

To use the Crop Disease Diagnosis API:

1. Obtain an API token by registering as a user and specifying your access level (`dev` or `farmer`).
2. Make a POST request to the API endpoint with the crop name and leaf image.
3. Receive a response indicating whether the leaf is healthy or diseased, along with disease details if applicable.


### Sample

#### Getting API key and registering username and level
![Screenshot 2023-08-16 011346](https://github.com/SIdR4g/Crop_Disease_Classification_API/assets/78850085/6e210f17-a28f-44dc-b727-3d07bddf588b)


#### Selecting the crop type and uploading image of the leaf to identify disease
![Screenshot 2023-08-16 011712](https://github.com/SIdR4g/Crop_Disease_Classification_API/assets/78850085/71359433-814c-4b04-b4a4-8e768da75eb3)
