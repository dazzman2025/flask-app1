pipeline {
    agent any

    environment {
        IMAGE_NAME = "damman2025/flask-demo"
        IMAGE_TAG = "v1"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
            }
        }
    }
}
