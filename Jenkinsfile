pipeline {
    agent any
    environment {
        DB_URI = credentials("DB_URI")
        SEC_KEY = credentials("SEC_KEY")
        DOCKERHUB_LOGIN = credentials("DOCKERHUB_LOGIN")
    }
    stages {

        stage('Test') {
            steps {
                sh "ls"
            }
        }

        stage('Build') {
            steps {
                sh "docker-compose build"

            }
        }
        stage('Push') {
            steps {
                sh "docker-compose push"
            }
        }
        stage('Ansible') {
            steps {
                sh "ls"
            }
        }
        stage('Deploy') {
            steps {
                sh "docker-compose pull && docker stack deploy --compose-file docker-compose.yaml cardgen"
            }
        }
    }
}