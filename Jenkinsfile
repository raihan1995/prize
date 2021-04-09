pipeline {
    agent any
    environment{
        DATABASE_URI = credentials("DATABASE_URI")
    }
    stages{
        stage('Testing'){
            steps{
                sh 'bash ./scripts/apptest.sh'
            }
        }
        stage('Build'){
            steps{
                sh 'docker-compose build'
            }
        }
        stage('Push'){
            steps{
                sh 'docker-compose push'
            }
        }
        stage('Swarm Configuration'){
            steps{
                sh 'cd ansible && ansible-playbook -i inventory.yaml playbook.yaml'
            }
        }
        stage('Deploy'){
            steps{ 
                sh 'bash ./scripts/appdeploy.sh'
            }
        }
    }
}