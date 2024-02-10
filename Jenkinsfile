pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout your code from version control
                    echo 'Stage 1: Checkout code in GitHub (scm)'
                    checkout scm
                }
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    // Install dependencies
                    echo 'Stage 2a: Install package dependencies'
                    //bat 'pip install -r requirements.txt'
                    bat 'python --version'
                    bat 'pip --version'

                    // Run unit tests using pytest
                    echo 'Stage 2b: Run unit tests'
                    //sh 'pytest'
                    //sh 'python -m unittest discover -s tests'    
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image and push to a registry
                    //sh 'docker build -t your-image-name .'
                    //sh 'docker push your-image-name'
                    echo 'Docker'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy your application (e.g., start Docker container)
                    //sh 'docker run -d -p 8080:8080 your-image-name'
                    echo 'Deploy'
                }
            }
        }
    }
}
