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
            }
        }
        stage('Swarm Configuration'){
            //Ansible
        }
        stage('Deploy'){
            steps{ sh 'docker-compose push'
            }
        }
        stage('Cleanup'){
            // do cleanup
        }
    }
}