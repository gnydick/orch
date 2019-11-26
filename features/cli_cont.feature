### Created by gnydick at 5/8/18
Feature: CLI api

Scenario: create and get
  Given create "id" "application" "testapp" via cli
  When get "application" "testapp" via cli
  Then delete "application" "testapp" via cli




Scenario: add to one to many
  Given create "id" "application" "testapp" via cli
  Given create "name" "stack" "teststack1" in "application_id" "testapp" via cli
  Given create "name" "service" "testservice1" in "stack_id" "testapp:teststack1" via cli
  Given create service_config "testservice_config" for "testapp:teststack1:testservice1" via cli
  When modify "service_config" "testapp:teststack1:testservice1:testservice_config" "service_config" "Hello" via cli
  Then delete "service_config" "testapp:teststack1:testservice1:testservice_config" via cli
  Given create environment "testenv" via cli
  Given create k8s_cluster "cluster1" in "testenv" via cli
  Given create deployment for service "testapp:teststack1:testservice1" in k8s "testenv:cluster1:k8s" via cli
  Given create "id" "config_type" "testcfgtype" via cli
  Given create config "testconfig" type "testcfgtype" for deployment "testenv:cluster1:k8s:testapp:teststack1:testservice1:default" tagged "tag" via cli
  Given create "id" "provider" "testprov" via cli
  Given create "name" "region" "testregion" in "provider_id" "testprov" via cli
  Given create "name" "zone" "testzone1" in "region_id" "testprov:testregion" via cli
  Then delete "zone" "testprov:testregion:testzone1" via cli
  Then delete "region" "testprov:testregion" via cli
  Then delete "provider" "testprov" via cli
  Then delete "config" "testenv:cluster1:k8s:testapp:teststack1:testservice1:default:testcfgtype:testconfig:tag" via cli
  Then delete "config_type" "testcfgtype" via cli
  Then delete "deployment" "testenv:cluster1:k8s:testapp:teststack1:testservice1:default" via cli
  Then delete "k8s_cluster" "testenv:cluster1:k8s" via cli
  Then delete "environment" "testenv" via cli
  Then delete "service" "testapp:teststack1:testservice1" via cli
  Then delete "stack" "testapp:teststack1" via cli
  Then delete "application" "testapp" via cli

Scenario: add to many to many
  Given create "id" "application" "testapp" via cli
  Given create "name" "stack" "teststack1" in "application_id" "testapp" via cli
  Given create "name" "stack" "teststack2" in "application_id" "testapp" via cli
  Given create "name" "service" "testservice1" in "stack_id" "testapp:teststack1" via cli
  Given create "name" "service" "testservice2" in "stack_id" "testapp:teststack1" via cli
  Given create "name" "service" "testservice1" in "stack_id" "testapp:teststack2" via cli
  Given create "name" "service" "testservice2" in "stack_id" "testapp:teststack2" via cli
  Given create environment "testenv" via cli
  Given create k8s_cluster "cluster1" in "testenv" via cli
  Given create "id" "provider" "testprov" via cli
  Given create "name" "region" "testregion" in "provider_id" "testprov" via cli
  Given create "name" "zone" "testzone1" in "region_id" "testprov:testregion" via cli
  Given create "name" "zone" "testzone2" in "region_id" "testprov:testregion" via cli
  Given create "name" "zone" "testzone3" in "region_id" "testprov:testregion" via cli
  Given create deployment for service "testapp:teststack1:testservice1" in k8s "testenv:cluster1:k8s" via cli

  When add_to_collection "testprov:testregion:testzone1" "1" to "zones" on "deployment" "testenv:cluster1:k8s:testapp:teststack1:testservice1:default" via cli
  When add_to_collection "testprov:testregion:testzone2" "2" to "zones" on "deployment" "testenv:cluster1:k8s:testapp:teststack1:testservice1:default" via cli
  When add_to_collection "testprov:testregion:testzone3" "3" to "zones" on "deployment" "testenv:cluster1:k8s:testapp:teststack1:testservice1:default" via cli

  Then query something "application" "id" "like" "testap%"
  Then query something "stack" "name" "like" "testst%"
  Then query something "stack" "id" "like" "testapp%" expect "2"
  Then query something "service" "name" "like" "tests%" expect "4"
  Then query something "service" "id" "like" "testapp:teststack1%" expect "2"
  Then query something "service" "id" "like" "testapp:teststack2%" expect "2"
  Then query something "service_config" "id" "like" "testmod%" expect "3"



  Then del_from_collection "testprov:testregion:testzone3" "3" to "zones" on "deployment" "testenv:cluster1:k8s:testapp:teststack1:testservice1:default" via cli
  Then del_from_collection "testprov:testregion:testzone2" "2" to "zones" on "deployment" "testenv:cluster1:k8s:testapp:teststack1:testservice1:default" via cli
  Then del_from_collection "testprov:testregion:testzone1" "1" to "zones" on "deployment" "testenv:cluster1:k8s:testapp:teststack1:testservice1:default" via cli
  Then delete "zone" "testprov:testregion:testzone1" via cli
  Then delete "zone" "testprov:testregion:testzone2" via cli
  Then delete "zone" "testprov:testregion:testzone3" via cli
  Then delete "region" "testprov:testregion" via cli
  Then delete "provider" "testprov" via cli
  Then delete "config" "testenv:cluster1:k8s:testapp:teststack1:testservice1:default:testcfgtype:testconfig:tag" via cli
  Then delete "config_type" "testcfgtype" via cli
  Then delete "deployment" "testenv:cluster1:k8s:testapp:teststack1:testservice1:default" via cli
  Then delete "k8s_cluster" "testenv:cluster1:k8s" via cli
  Then delete "environment" "testenv" via cli
  Then delete "service" "testapp:teststack2:testservice2" via cli
  Then delete "service" "testapp:teststack2:testservice1" via cli
  Then delete "service" "testapp:teststack1:testservice2" via cli
  Then delete "service" "testapp:teststack1:testservice1" via cli
  Then delete "stack" "testapp:teststack2" via cli
  Then delete "stack" "testapp:teststack1" via cli
  Then delete "application" "testapp" via cli