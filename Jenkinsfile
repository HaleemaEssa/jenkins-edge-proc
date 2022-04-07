pipeline {
  agent any
  environment {
        DOCKERHUB_CREDENTIALS=credentials('haleema-dockerhub')
    }
  
  stages {
    stage('Login to Dockerhub') {
           steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        } 
stage('On-Edge2') {
          steps {
            sh 'echo "edge3"'
            git branch: 'main', url: 'https://github.com/HaleemaEssa/jenkins-edge3.git'
            sh 'docker build -t haleema/docker-edge3:latest .'
            //sh 'sleep 10'
            //sh 'docker stop  haleema/docker-edge1; docker rm  haleema/docker-edge3'
            sh 'docker run -v "${PWD}:/data" -t haleema/docker-edge3'
            

          }
        } 
  }
}
