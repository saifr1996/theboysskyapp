pipeline {
    agent any

    stages {
        stage('Build and Push Docker Image') {
            steps {
                sh 'docker build -t "jonnobrow/team2flask:latest" .'
                withCredentials([usernamePassword(credentialsId: 'ac76b062-eac4-4d35-85dd-2779836c84c9', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'docker login -u "${DOCKER_USER}" -p "${DOCKER_PASS}"'
                }
                sh 'docker push "jonnobrow/team2flask:latest"'
            }
        }
        stage('Force Re-deployment of ECS Service') {
            steps {
                sh 'aws ecs update-service --cluster showcase --service theboysskyproject --task-definition theboysskyproject --region eu-west-1 --force-new-deployment'
            }
        }
    }
}
