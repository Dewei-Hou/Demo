pipeline {
    agent {
        label 'docker-agent'
    }

    stages {
        stage('Check Out') {
            steps {
                echo 'checkout 完成'
            }
        }

        stage('Build') {
            steps {
                echo '開始建置...'
                sh 'python3 app.py'
            }
        }

        stage('Test') {
            steps {
                echo '開始測試...'
                sh 'python3 test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo '部署完成！'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline 成功！'
        }
        failure {
            echo '❌ Pipeline 失敗！'
        }
    }
}