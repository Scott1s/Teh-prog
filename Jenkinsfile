pipeline {
    agent {
        docker {
            image 'alpine:3.21'
			args '-u root:root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    triggers {
		cron('H/30 * * * *')
        pollSCM('H * * * *')
    }
    

    environment {
        DOCKER_IMAGE    = 'sott1s/lab4'
		DOCKER_CREDS_ID = 'dockerhub-credentials'
    }

    options {
        timestamps()
    }

    stages {

        stage('[Jenkins] :: Check scm') {
            agent any
            steps {
                checkout scm
            }
        }

        stage('[Application] :: Install dependencies') {
            steps {
                sh 'apk add --update python3  py3-xml-runner'
            }
        }

        stage('[Application] :: Build') {
            steps {
                echo "Building ...${BUILD_NUMBER}"
                echo "Build completed"
            }
        }

        stage('[Application] :: Test') {
            steps {
                echo "Testing ...${BUILD_NUMBER}"
                sh 'python3 test_notebook.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Application testing successfully completed"
                }
                failure {
                    echo "Oooppss!!! Tests failed!"
                }
            }
        }

        stage('[Application] :: Archive') {
            steps {
                archiveArtifacts artifacts: 'notebook.py', fingerprint: true
            }
        }

		stage('[Docker] :: Install docker') {
            steps {
                sh 'apk add --no-cache docker'
            }
        }
		
		stage('[Docker] :: Build image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .'
                    sh 'docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest'
				}
            }
        }
		
		stage('[Docker] :: Push to https://hub.docker.com/') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDS_ID, passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                        sh 'docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}'
                        sh 'docker push ${DOCKER_IMAGE}:latest'
                    }
                }
            }
        }
		
		stage('[Docker] :: Cleanup') {
             steps {
                 sh 'docker rmi ${DOCKER_IMAGE}:${BUILD_NUMBER} || true'
                 sh 'docker rmi ${DOCKER_IMAGE}:latest || true'
             }
        }
    }
}


