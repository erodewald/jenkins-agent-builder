pipeline {
    agent { 
        docker {
            image "agent-builder:latest"
            args "-v /var/run/docker.sock:/var/run/docker.sock"
        }
    }
    environment {
        AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
        AWS_DEFAULT_REGION = 'us-east-1'
        VERSION = sh(returnStdout: true, script: 'generate-version')
    }
    stages {
        stage('Git Tag Version')
        {
            steps {
                // Pull into an external script for more generic use.
                withCredentials([usernamePassword(credentialsId: 'FOD_AWS_STASH', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    sh('git config --global user.email "none@snapfitness.com"')
                    sh('git config --global user.name "fodaws"')
                    sh("git tag -a release/$VERSION -m 'Jenkins deploy tag'")
                    // Use git remote get-url origin to get the URL at some point
                    sh('git push https://${GIT_USERNAME}:${GIT_PASSWORD}@stash.liftbrands.com/scm/fod/jenkins.git --tags')
                }
            }
        }
        stage('Build Docker Images') {
            steps {
                slackSend (color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
                sh "build-docker-images ${VERSION}"
            }
        }
        stage('Push Images to ECS') {
            steps {
                sh "push-docker-images ${VERSION}"
            }
        }
    }
    post {
        success {
            slackSend (color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
        failure {
            slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
    }
}