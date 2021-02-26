pipeline {
    agent any
    stages {
<<<<<<< HEAD

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
                sh "ansible-playbook -i inventory.yaml playbook.yaml"
=======
        stage('Build') {
            steps {
                //
            }
        }
        stage('Test') {
            steps {
                //
>>>>>>> 1776e768350bbd77a9b031081b98abf34ad03962
            }
        }
        stage('Deploy') {
            steps {
<<<<<<< HEAD
                sh "docker-compose pull && docker stack deploy --compose-file docker-compose.yaml cardgen"
=======
                //
>>>>>>> 1776e768350bbd77a9b031081b98abf34ad03962
            }
        }
    }
}