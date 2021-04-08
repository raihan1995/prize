pipeline {
    agent any
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
                sh 'bash ./scripts/apptest.sh'
            }
        }
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