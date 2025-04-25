pipeline {
    agent any
    
    environment {
        // Define any environment variables you need here
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    // Ensure Python environment and install dependencies from requirements.txt
                    sh 'python3 -m venv venv'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests (using pytest or unittest)
                    sh './venv/bin/python -m pytest tests/test_dummy.py'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Any additional build steps if needed
                    echo 'Building the chatbot project...'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Optional: Add deployment steps here
                    echo 'Deploying chatbot application...'
                }
            }
        }
    }

    post {
        always {
            // Actions to perform after pipeline run (e.g., clean up)
            echo 'Pipeline completed!'
        }
        success {
            // Actions to perform on successful pipeline execution
            echo 'Pipeline was successful!'
        }
        failure {
            // Actions to perform if pipeline fails
            echo 'Pipeline failed!'
        }
    }
}
