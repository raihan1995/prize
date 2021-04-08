pipeline {
    agent any
    stages{
        stage('Testing'){
            steps{
                sh './scripts/apptest.sh'
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
        // stage('Swarm Configuration'){
        //     steps{
        //         //Ansible-playbook
        //     }
        // }
        // stage('Deploy'){
        //     steps{ 
        //         //sh 'docker-compose push'
        //     }
        // }
        // stage('Cleanup'){
        //     steps{
        //         // do cleanup
        //     }
        // }
    }
}