pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout your code from version control
                    checkout scm
                    echo 'Stage 1: Checkout code in GitHub (scm)'
                }
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    // Build and run your tests
                    //sh 'pip install -r requirements.txt'
                    //sh 'python -m unittest discover -s tests'
                    echo 'buildNtest'
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
