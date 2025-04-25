pipeline {
  agent {
    docker {
      image 'python:3.10'
      args '-p 8501:8501'
    }

  }
  stages {
    stage('Clone') {
      parallel {
        stage('Clone') {
          steps {
            git 'https://github.com/your-username/your-repo.git'
          }
        }

        stage('Shell Script') {
          steps {
            sh '''git clone https://github.com/chandra0013/chatbot-streamlit-app.git
cd chatbot-streamlit-app
'''
          }
        }

      }
    }

    stage('Install Requirements') {
      parallel {
        stage('Install Requirements') {
          steps {
            sh 'pip install -r requirements.txt'
          }
        }

        stage('Shell Script') {
          steps {
            sh '''cd chatbot-streamlit-app
pip install -r requirements.txt
'''
          }
        }

      }
    }

    stage('Run Streamlit App') {
      parallel {
        stage('Run Streamlit App') {
          steps {
            sh 'streamlit run app.py --server.port=8501'
          }
        }

        stage('Shell Script') {
          steps {
            sh '''cd chatbot-streamlit-app
streamlit run app.py --server.port=8501
'''
          }
        }

      }
    }

  }
}