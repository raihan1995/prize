pipeline {
    agent any
    stages{
        // stage('Testing'){
        //     steps{
        //         sh '''
        //             cd prize/service1
        //             pip3 install -r requirements.txt
        //             cd tests
        //             pytest --cov=app
        //             cd ../..
        //             '''
        //     }
        // }
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