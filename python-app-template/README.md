# Template for python application

 * incl. multi-stage Dockerfile, helm chart, jenkins-ii configuration

## Requirements
 * `cookiecutter`

## Example usage
```
$ cookiecutter python-app-template 
app_name [test-app]: 
maintainer [noone <noone@gooddata.com>]: 
description [description]: 
base_package [test_app]: 
docker_image_name [test-app]: 
docker_user_id [1112]: 
helm_chart_name [test-app]: 
k8s_values_first_level [application]: 
k8s_values_second_level [component]: 
target_github_repository []: 
```

See the generated structure under `test-app` directory.

Details how to build / run application locally or deploy it in k8s is in generated
README file.
