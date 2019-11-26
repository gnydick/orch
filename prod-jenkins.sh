#!/usr/bin/env bash


stack=infra:build_and_deploy
service=jenkins
deployment=prod:$stack:$service:default

DOCKER_IMG=$(curl -s http://orch/api/rest/v1/service/$stack:$service | jq -r .docker_image_url)

DOCKER_TAG=$(curl -s http://orch/api/rest/v1/deployment/$deployment | jq -r .version)

mkdir -p ${service}/templates
curl -s http://orch/api/rest/v1/module/jenkins_helm_chart | jq -r .module > jenkins/templates/template.yaml
curl -s http://orch/api/rest/v1/module/jenkins_helm_chart | jq -r .defaults > jenkins/templates/_helpers.tpl
curl -s http://orch/api/rest/v1/config/prod:infra:build_and_deploy:jenkins:default:values.yaml:prodjenkins:default | jq -r .config > jenkins/values.yaml
curl -s http://orch/api/rest/v1/config/prod:infra:build_and_deploy:jenkins:default:chart.yaml:prodjenkins:default | jq -r .config > jenkins/Chart.yaml