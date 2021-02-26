pipeline {
    agent any
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
                sh "ansible-playbook -i inventory.yaml playbook.yaml"
            }
        }
        stage('Deploy') {
            steps {
                sh "docker-compose pull && docker stack deploy --compose-file docker-compose.yaml cardgen"
            }
        }
    }
}