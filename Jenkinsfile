pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup') {
            steps {
                bat '''
                echo Configurando o ambiente...
                python -m venv venv
                venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Script') {
            steps {
                bat '''
                echo Executando o script principal...
                venv\\Scripts\\activate
                python main.py
                '''
            }
        }
    }
    post {
        always {
            echo "Pipeline finalizado!"
        }
    }
}
