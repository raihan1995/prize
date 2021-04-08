pipeline {
    agent any
    stages{
        stage('Testing'){
            steps{
                sh '''
                    sudo apt update
                    sudo apt install -y python3 virtualenv
                    virtualenv -p python3 venv
                    source venv/bin/activate
                    pip3 install -r requirements.txt
                    cd service1/tests
                    pytest test_app.py
                    pytest --cov=app
                    cd ../..
                    '''
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