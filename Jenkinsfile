pipeline {
    agent any

    environment {
        APP_NAME = 'cloudops-ticket-analyzer'
        IMAGE_NAME = 'cloudops-ticket-analyzer'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling source code from GitHub...'
                checkout scm
            }
        }

        stage('Python Setup and Unit Tests') {
            steps {
                echo 'Installing Python dependencies and running unit tests...'
                sh '''
                    cd app
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest
                '''
            }
        }

        stage('Terraform Format and Validate') {
            steps {
                echo 'Checking Terraform formatting and validating IaC...'
                sh '''
                    cd terraform
                    terraform fmt -check
                    terraform init -backend=false
                    terraform validate
                '''
            }
        }

        stage('Checkov IaC Security Scan') {
            steps {
                echo 'Scanning Terraform code for security misconfigurations...'
                sh '''
                    checkov -d terraform || true
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                sh '''
                    docker build -t $IMAGE_NAME:latest .
                '''
            }
        }

        stage('Trivy Container Scan') {
            steps {
                echo 'Scanning Docker image for vulnerabilities...'
                sh '''
                    trivy image $IMAGE_NAME:latest || true
                '''
            }
        }

        stage('Deployment Gate') {
            steps {
                echo 'All checks complete. Deployment would happen here after approval.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Check the Jenkins console output.'
        }
    }
}
