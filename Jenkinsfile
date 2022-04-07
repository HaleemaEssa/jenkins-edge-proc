pipeline {
    agent any
    stages {
        stage('GitClone') {
            steps {
                git branch: 'main', url: 'https://github.com/HaleemaEssa/jenkins-edge3.git'
            }
        }
    stage('Login to Dockerhub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        } 
        
    stage('runimage') {
         
            steps {
                sh 'docker run -v "${PWD}:/data" -t haleema/docker-edge3' 
            }
         }    
    }
    }
