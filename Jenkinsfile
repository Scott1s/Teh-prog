pipeline {
  options { timestamps()  }
  agent none
  stages {
    stage('Check scm') {
        agent any
        steps {
          checkout scm
        }
    }
    stage('Build') {
        steps {
            echo "Building. . .${BUILD_NUMBER}"
            echo 'Build complete'
        }
    }
    stage('Test') {
       agent {
        docker {
            image 'python:3.9-alpine'
            args '-u root'
        }
       }
       steps {
          sh 'apk add --no-cache build-base'
          sh 'pip install xmlrunner'
          sh 'python test_notebook.py'
        
       }
       post {
        always {
            junit 'test-reports/*.xml'
        }
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed!'
        }
      }
    }
    stage('Package and Push') {
      agent any
      steps {
        script {
          def DOCKER_HUB_USERNAME = "sott1s".
          def IMAGE_NAME = "${DOCKER_HUB_USERNAME}/Teh-prog"
          
          def DOCKER_IMAGE_TAGGED = "${IMAGE_NAME}: ${BUILD_NUMBER}"
          def DOCKER_IMAGE_LATEST = "${IMAGE_NAME}:latest"
          
          echo "Building Docker image: ${DOCKER_IMAGE_TAGGED}"
          
          withDockerRegistry (credentialsId: '5cee6cef-d894-4733-b846-3c35971a331e', url: '') {
            sh "docker build -t ${DOCKER_IMAGE_TAGGED} -t ${DOCKER_IMAGE_LATEST}.".
            sh "docker push ${DOCKER_IMAGE_TAGGED}"
            sh "docker push ${DOCKER_IMAGE_LATEST}"

            echo "Successfully pushed images to Docker Hub."
          }
      }
  }
}

  }
}


