pipeline {
  agent any
   stages {
    stage ('Build') {
      steps {
        sh 'rm -rf ./kura_test_repo/cypress2'
        sh '''
          npm install
          '''
        sh '''#!/bin/bash
        python3 -m venv test3
        source test3/bin/activate
        pip install pip --upgrade
        pip install -r requirements.txt
        export FLASK_APP=application
        flask run &
        '''
      } 
    }
    stage ('test') {
      steps {
        agent {
        label 'React-dev'
      }
      steps {
        sh ''' 
          npm install cypress
          npm install mocha
          npx cypress run --spec ./cypress/integration/test.spec.js
          '''
        }
        post {
          always {
            junit 'results/cypress-report.xml'
          }
            
        }
        sh '''#!/bin/bash
        source test3/bin/activate
        py.test --verbose --junit-xml test-reports/results.xml
        '''
      }
      post{
        always {
          junit 'test-reports/results.xml'
        }
      } 
    }
  } 
}