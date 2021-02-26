pipeline {
    agent any
    stages {
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6932e9c364e1285edc90a8fa4d69cccf22c071c6

        stage('Test') {
            steps {
                sh "ls"
            }
        }
<<<<<<< HEAD
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
=======
>>>>>>> 6932e9c364e1285edc90a8fa4d69cccf22c071c6
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
<<<<<<< HEAD
                //
>>>>>>> 1776e768350bbd77a9b031081b98abf34ad03962
=======
                sh "ls"
>>>>>>> 6932e9c364e1285edc90a8fa4d69cccf22c071c6
            }
        }
        stage('Deploy') {
            steps {
<<<<<<< HEAD
<<<<<<< HEAD
                sh "docker-compose pull && docker stack deploy --compose-file docker-compose.yaml cardgen"
=======
                //
>>>>>>> 1776e768350bbd77a9b031081b98abf34ad03962
=======
                sh "docker stack deploy --compose-file docker-compose.yaml cardgen"
>>>>>>> 6932e9c364e1285edc90a8fa4d69cccf22c071c6
            }
        }
    }
}