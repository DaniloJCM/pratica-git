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

        stage('Code Coverage Test') {
            steps {
                echo 'Rodando os testes com cobertura...'
                bat 'coverage run teste.py'
                bat 'coverage xml -o coverage.xml'
                bat 'coverage report'
            }
        }

    }

    post {
        always {
            recordCoverage(
                tools: [[parser: 'COBERTURA', pattern: 'coverage.xml']]
            )
        }
        success {
            echo 'Build e teste executados com SUCESSO!'
        }
        failure {
            echo 'FALHA na build ou nos testes.'
        }
    }
}