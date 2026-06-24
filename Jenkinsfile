pipeline {
    agent any

    environment {
        IMAGE_NAME = "dazzman2025/flask-demo"
        IMAGE_TAG = "v1"
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'git@github.com:dazzman2025/flask-app1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask_app1:v2 .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
            }
        }

    }
}
