// def VERSION = 'UNKNOWN'

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
        // stage('generate-version') {
        //     steps {
        //         script {
                    
        //         }
        //     }
        // }
        stage('build') {
            steps {
                echo "Test: ${VERSION}"
                sh "echo ${VERSION}"
                // slackSend (color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
                // sh 'build-docker-images "$VERSION"'
            }
        }
        // stage('deploy') {
        //     steps {
        //         sh 'push-docker-images "$VERSION"'
        //         // sh 'git tag release/$VERSION'
        //         // sh 'git push origin master'
        //         // git branch: 'lts-1.532', credentialsId: '82aa2d26-ef4b-4a6a-a05f-2e1090b9ce17', url: 'git@github.com:jenkinsci/maven-plugin.git'
        //     }
        // }
    }
    // post {
    //     success {
    //         slackSend (color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
    //     }
    //     failure {
    //         slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
    //     }
    // }

}