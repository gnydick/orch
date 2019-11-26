node {
    stage("Build") {
        checkout scm
        sh "docker build -t orch:${BUILD_NUMBER} ."
    }
}

