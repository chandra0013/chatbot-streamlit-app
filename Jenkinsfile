pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-p 8501:8501'
        }
    }
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Streamlit App') {
            steps {
                sh 'streamlit run app.py --server.port=8501'
            }
        }
    }
}
