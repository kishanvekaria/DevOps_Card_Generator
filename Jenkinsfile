pipeline {
    agent any
    environment {
        DB_URI = credentials("DATABASE_URI")
        SEC_KEY = credentials("SEC_KEY")
        DOCKER_CREDENTIALS = credentials("docker-hub-credentials")
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