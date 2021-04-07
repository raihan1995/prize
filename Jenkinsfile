pipeline {
    agent any
    stages{
        stage('Clone'){
            steps{
                sh 'git clone https://github.com/raihan1995/prize'
            }
        }
        stage('Testing'){
            //add testing script
        }
        stage('Build'){
            steps{
                sh 'cd prize'
                sh 'docker-compose down --rmi all'
                sh 'docker-compose build'
                sh 'docker-compose up -d'
            }
        }
        stage('Swarm Configuration'){
            //Ansible
        }
        stage('Deploy'){
            steps{ //sh 'docker-compose push'

            }
        }
        stage('Cleanup'){
            // do cleanup
        }
    }
}