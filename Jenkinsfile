
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\Student\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python application'
                bat '"%PYTHON%" -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Executing automated tests'
                bat '"%PYTHON%" -m unittest app'
            }
        }

        stage('Run Application') {
            steps {
                bat '"%PYTHON%" app.py'
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully'
        }

        failure {
            echo 'CI Pipeline failed'
        }
    }
}
