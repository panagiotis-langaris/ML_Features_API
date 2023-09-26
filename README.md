# Get_Features FastAPI Application
A FastAPI application that can be used to extract features from a given data set using the Featuretools framework.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Helpful Screenshots](#helpful-screenshots)

## About

[Provide a brief description of your application. Explain its purpose and any unique features.]

## Features

- [List some key features of your application.]

## Getting Started

### Prerequisites

The required packages are listed inside the requirements.txt file.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/optasia-fastapi.git
   cd optasia-fastapi
   
In Visual Studio Code terminal, run the below:

### 1. Create a virtual environment and activate it:
   
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

### 2. Install the dependencies:
pip install -r requirements.txt

### 3. Build Docker image and run the container

docker build -t get_features_app .
docker run -p 80:80 get_features_app

## Usage

After starting the container, you can start consuming the API:


- Check the API Documentation by browsing to at http://localhost/docs
  Here you can also consume the API endpoints, or you can use Postman client instead.
- In Docker Terminal, run the following command to run the unit tests. It should return 2 passed tests.
  pytest test_main.py
- In Docker Files, you can see the log file inside the ''app'' folder (/app/app.log). The requests that the API received are kept here.


## Helpful Screenshots
![postman_get_features_response](https://github.com/panagiotis-langaris/ML_Features_API/assets/16323614/a1c06da8-c697-4591-bcd2-6be0aa748431)
![api_documentation](https://github.com/panagiotis-langaris/ML_Features_API/assets/16323614/3964aec9-fb03-4dce-a632-e36fb41d1df8)
![docker_image](https://github.com/panagiotis-langaris/ML_Features_API/assets/16323614/e681c1aa-e0d8-4baf-89be-8aedbcd7d43a)
![docker_container_terminal](https://github.com/panagiotis-langaris/ML_Features_API/assets/16323614/b4852f27-740c-418b-8516-f3f0ad58af11)


