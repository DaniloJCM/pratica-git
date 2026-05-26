pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Rodando arquivo temperatura.py ...'
                bat 'python temperatura.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Rodando o arquivo teste.py ...'
                bat 'python teste.py'
            }
        }

    }

    post {
        success {
            echo 'Build e teste executados com SUCESSO!'
        }
        failure {
            echo 'FALHA na build ou nos testes.'
        }
    }
}