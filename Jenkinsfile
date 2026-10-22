pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python --version'
                bat 'python -m py_compile app.py test_app.py'
                bat 'python app.py'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest -v'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully.'
        }
        failure {
            echo 'CI pipeline failed. Review the stage logs above.'
        }
    }
}
