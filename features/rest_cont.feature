#### Created by gnydick at 5/8/18
Feature: REST api


Scenario: environments and deployments, configs, and service_configs
  Given provider "testprov" can be created via rest
  And region "testregion" can be created for provider "testprov" via rest
  And zone "testzone" can be created for region "testprov:testregion" via rest
  And zone "testzone2" can be created for region "testprov:testregion" via rest
  And application "testapp" can be created via rest
  And stack "teststack" can be created for app "testapp" via rest
  And service "testservice" can be created for stack "testapp:teststack" via rest
  And environment "testenv" can be created via rest
  And create k8s_cluster "cluster1" in "testenv" via rest
  And create deployment at "testenv:cluster1:k8s" for "testapp:teststack:testservice" tagged "default" with defaults "{}" at version "1" via rest

  And service_config "testservice_config" can be created for service "testapp:teststack:testservice" via rest
  And service_config "testservice_config2" can be created for service "testapp:teststack:testservice" via rest
  And config_type "testcfgtype" can be created via rest
  Given config "testconfig" of "testcfgtype" can be created for deployment "testenv:cluster1:k8s:testapp:teststack:testservice:default" tagged "tag" via rest

  And update "version" for "deployment" "testenv:cluster1:k8s:testapp:teststack:testservice:default" to "2" via rest
  When add first "zones" "testprov:testregion:testzone" on "deployment" "testenv:cluster1:k8s:testapp:teststack:testservice:default" via rest
  And add second "zones" "testprov:testregion:testzone2" on "deployment" "testenv:cluster1:k8s:testapp:teststack:testservice:default" via rest


  Then remove second "zones" "testprov:testregion:testzone2" on "deployment" "testenv:cluster1:k8s:testapp:teststack:testservice:default" via rest
  And remove first "zones" "testprov:testregion:testzone" on "deployment" "testenv:cluster1:k8s:testapp:teststack:testservice:default" via rest

  When delete "config" "testenv:cluster1:k8s:testapp:teststack:testservice:default:testcfgtype:testconfig:tag" via rest
  Then delete "config_type" "testcfgtype" via rest

  Then delete "deployment" "testenv:cluster1:k8s:testapp:teststack:testservice:default" via rest
  Then delete "k8s_cluster" "testenv:cluster1:k8s" via rest
  Then delete "environment" "testenv" via rest
  Then delete "zone" "testprov:testregion:testzone" via rest
  Then delete "zone" "testprov:testregion:testzone2" via rest
  Then delete "region" "testprov:testregion" via rest
  Then delete "provider" "testprov" via rest
  And delete "service_config" "testapp:teststack:testservice:testservice_config" via rest
  And delete "service_config" "testapp:teststack:testservice:testservice_config2" via rest
  And delete "service" "testapp:teststack:testservice" via rest
  And delete "stack" "testapp:teststack" via rest
  And delete "application" "testapp" via rest

