pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Allocate Docker') {
      steps {
        dockerNode(image: 'michalleszczynski/magic-tale:2.0') {
          sh 'black *'
          sh 'py.test'
        }

      }
    }
  }
}