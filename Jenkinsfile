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
                sh 'cd ansible && ansible-playbook -i inventory.yaml playbook.yaml'
            }
        }
        // stage('Deploy'){
        //     steps{ 
        //         sh 'docker stack deploy --compose-file docker-compose.yaml passwordapp'
        //     }
        // }
        // stage('Cleanup'){
        //     steps{
        //         // do cleanup
        //     }
        // }
    }
}