# Get_Features FastAPI Application
A FastAPI application that can be used to extract features from a given data set using the Featuretools framework.

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Helpful Screenshots](#helpful-screenshots)

## About

This repository contains the Get_Features FastAPI application, which is designed to extract features from a provided dataset using the Featuretools framework. The application offers a set of API endpoints that allow users to perform feature extraction and retrieve the resulting features in a structured format.
The API comes with unit testing to ensure the API is operating promptly and log configuration to monitor the API.

## Getting Started

### Prerequisites

The required packages are listed inside the requirements.txt file.

### Installation

After downloading or cloning all the files, launch Visual Studio Code and change directory (cd) to the downloaded folder.
In Visual Studio Code terminal, run the below:

#### 1. Create a virtual environment and activate it:

  ```bash
  python -m venv getfeatures
  .\getfeatures\Scripts\activate  # (On Windows)
  ```
#### 2. Build Docker image and run the container

```bash
docker build -t get_features_app .
docker run -p 80:80 get_features_app
```

## Usage

After starting the container, you can start consuming the API:


- Check the API Documentation by browsing to at http://localhost/docs
  Here you can also consume the API endpoints, or you can use Postman client instead.
- In Docker Terminal, run the following command to run the unit tests. It should return 2 passed tests.
  ```bash
  pytest test_main.py
- In Docker Files, you can see the log file inside the ''app'' folder (/app/app.log). The requests that the API received are kept here.


## Helpful Screenshots
![api_documentation](https://github.com/panagiotis-langaris/ML_Features_API/assets/16323614/3964aec9-fb03-4dce-a632-e36fb41d1df8)

![postman_get_features_response](https://github.com/panagiotis-langaris/ML_Features_API/assets/16323614/a1c06da8-c697-4591-bcd2-6be0aa748431)

![docker_image](https://github.com/panagiotis-langaris/ML_Features_API/assets/16323614/e681c1aa-e0d8-4baf-89be-8aedbcd7d43a)

![docker_container_terminal](https://github.com/panagiotis-langaris/ML_Features_API/assets/16323614/b4852f27-740c-418b-8516-f3f0ad58af11)


