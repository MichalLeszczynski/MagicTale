pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Checking formatting') {
      steps {
        sh 'black . --check --include \\.py'
      }
    }
     stage('Running unit tests') {
      steps {
        sh 'py.test -v'
      }
    }
  }
}