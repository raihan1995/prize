pipeline {
    agent any
    stages{
        stage('Testing'){
            //add testing script
            echo 'Testing'
        }
        stage('Build'){
            sh 'docker-compose down --rmi all'
            sh 'docker-compose build'
        }
        stage('Swarm Configuration'){
            //Ansible
        }
        stage('Deploy'){
            sh 'docker-compose push'
        }
        stage('Cleanup'){
            // do cleanup
        }
    }
}