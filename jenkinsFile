pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                // Instalar as dependências do projeto
                sh 'pip install -r requirements.txt' // Use se houver dependências, mesmo que seja vazio
            }
        }
        stage('Run Tests') {
            steps {
                // Rodar o script de testes usando unittest
                sh 'python -m unittest -v test_math.py'
            }
        }
    }
}
