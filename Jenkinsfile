pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }
	
    stages {
        stage('Checkout') {
            steps {
		// Checkout your code from version control
		echo 'Stage 1: Checkout code in GitHub (scm)'
		// Checkout the code from GitHub using the Pipeline-Syntax- generated code snippet
		checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/panagiotis-langaris/ML_Features_API.git']])
            }
        }
        stage('Build environment') {
            steps {
		echo 'Stage 2: Build & activate virtual environment, and install dependencies'

		// Create and activate virtual environment
		//bat "${pythonExecutable} -m venv ${venvPath}"
		//bat "${venvPath}\\Scripts\\activate"
		
		// Install dependencies
		//bat "${pythonExecutable} --version"
		//bat "python --version"
		//bat "${venvPath}\\Scripts\\pip install -r requirements.txt"
		// Run Python file
		sh 'python3 main.py'
            }
        }
        stage('Unit tests') {
            steps {
		echo 'Stage 3: Run unit tests'
		// Run unit tests using pytest
		//sh 'pytest'
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
		// Deploy your application (e.g., start Docker container)
		//sh 'docker run -d -p 8080:8080 your-image-name'
		echo 'Deploy'
            }
        }
    }
}
