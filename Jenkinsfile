pipeline {
    agent any
    environment {
        DB_URI = credentials("DB_URI")
        SEC_KEY = credentials("SEC_KEY")
        DOCKERHUB_LOGIN = credentials("DOCKERHUB_LOGIN")
    }
    stages {
        stage('Test'){
            steps{
                sh './scripts/test.sh'
            }
        }
        stage('Build and Push'){
            steps{
                sh './scripts/build.sh'
            }
        }
        stage('Ansible'){
            steps{
                sh './scripts/ansible.sh'
            }
        }
        stage('Deploy'){
            steps{
                sh './scripts/deploy.sh'
            }
        }                   
    }
}