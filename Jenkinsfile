pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }
    tools {
        // Specify the name of the Python installation configured in Global Tool Configuration
        //tool 'AnacondaPython'
        jenkins.plugins.shiningpanda.tools.PythonInstallation tool: 'AnacondaPython'
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
        stage('Build environment') {
            steps {
                script {
                    echo 'Stage 2: Build & activate virtual environment, and install dependencies'
                    // Specify the path to Python executable
                    def pythonExecutable = "C:\\Users\\plang\\anaconda3\\python.exe"
					
                    // Specify the path for the virtual environment
                    def venvPath = "venv"

                    // Create and activate virtual environment
                    bat "${pythonExecutable} -m venv ${venvPath}"
                    bat "${venvPath}\\Scripts\\activate"

                    // Install dependencies
                    bat "${pythonExecutable} --version"
                    bat "python --version"
                    //bat "${venvPath}\\Scripts\\pip install -r requirements.txt"
                }
            }
        }
        stage('Unit tests') {
            steps {
                script {
                    // Run unit tests using pytest
                    echo 'Stage 3: Run unit tests'
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
