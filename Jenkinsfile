pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout your code from version control
                    checkout scm
                    echo 'checkout stage!'
                }
            }
        }
    }
}
