pipeline {
    agent any
    stages{
        stage('Testing'){
            //add testing script
        }
        stage('Build'){
            steps{
                sh 'docker-compose down --rmi all'
                sh 'docker-compose build'
                sh 'docker-compose up -d'
            }
        }
        stage('Push'){
            steps{
                sh 'docker-compose push'
            }
        }
        stage('Swarm Configuration'){
            //Ansible-playbook
        }
        stage('Deploy'){
            steps{ 
                sh 'docker-compose push'
            }
        }
        stage('Cleanup'){
            // do cleanup
        }
    }
}