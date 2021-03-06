# {{cookiecutter.app_name.replace('-', ' ').title()}} spring boot application

These instructions were generated by the `cookiecutter` template, feel free to update it based on actual application needs.

## Local development

### Requirements
 * {{cookiecutter.build_system}}
 * Java {{cookiecutter.java_version}}

### Build application and run tests
```
$ {%- if cookiecutter.build_system == 'gradle' %}./gradlew clean build{%- else %}./mvnw clean package{%- endif %}
```

### Start application
```
$ {%- if cookiecutter.build_system == 'gradle' %}./gradlew bootRun{%- else %}./mvnw spring-boot:run{%- endif %}
```

## Docker support
Docker build is already expecting the created "jar" file in build directory.

### Build docker image
```
$ docker build -t {{cookiecutter.app_name}} .
```

### Run application in docker
```
$ docker run -p {{cookiecutter.docker_application_port}}:{{cookiecutter.docker_application_port}} -it {{cookiecutter.app_name}}
```

## K8S support

Before proceeding, you should be aware of the k8s and CD basics.
Best place to start is [k8s developers guide](https://confluence.intgdc.com/display/plat/Kubernetes+Developers+Guideline)

### Continuous Deployment Integration
There is a generated file `.gdc-ii-config.yaml` and `Jenkinsfile` required
by our existing CD pipelines on [jenkins-ii](https://jenkins-ii.intgdc.com/).

If your repository is not yet configured, follow the steps described in
[k8s developers guide - ci-infra setup](https://confluence.intgdc.com/display/plat/Kubernetes+Developers+Guideline#KubernetesDevelopersGuideline-Step5-Definepipelinesinci-infrarepository).

To enable deployment of {{cookiecutter.helm_chart_name}} to our testing cluster,
you should update the [charts-config](https://github.com/gooddata/charts-config) repository.

More details can be found in [k8s developers guide - charts-config](https://confluence.intgdc.com/display/plat/Kubernetes+Developers+Guideline#KubernetesDevelopersGuideline-Step6-Defineserviceconfigurationincharts-configrepository).

### Testing of chart deployment on isolated k8s
You can deploy your own `k8s` instance type or `rat+k8s`. Alternatively you can
use local `minikube`.

To validate your application logic in chart, you can follow these steps:
 * build docker image and push it in [harbor](https://confluence.intgdc.com/display/plat/Kubernetes+Developers+Guideline#KubernetesDevelopersGuideline-DockerregistryforK8S)
```
$ docker login harbor.intgdc.com
$ docker tag {{cookiecutter.app_name}} harbor.intgdc.com/<your-namespace>/{{cookiecutter.app_name}}
$ docker push harbor.intgdc.com/<your-namespace>/{{cookiecutter.app_name}}
```
 * SSH to your k8s instance and clone the repository with the chart
```
$ ssh root@<k8s-instance-fqdn>
$ git clone git@github.com:<your-fork>/{{cookiecutter.target_github_repository}}.git
```
 * install the chart from git directory with custom image from harbor namespace
```
$ cd {{cookiecutter.target_github_repository}}/k8s/charts
$ helm upgrade --install {{cookiecutter.helm_chart_name}} {{cookiecutter.helm_chart_name}} \
    --set {{cookiecutter.k8s_values_first_level}}.{{cookiecutter.k8s_values_second_level}}.image.namespace=<your-namespace> \
    --wait --timeout 300
```
This will install the defined k8s objects in default namespaces (you can alternatively use
`--namespace <namespace>` in command above).
 * validate the created k8s objects
```
$ kubectl get pods
```

### Any issues?
Try to troubleshoot yourself, feel free to reach the [#proj-ii](https://app.slack.com/client/T02G0PHRH/C4JFVCW2V) slack channel or somebody
from II team when you are lost.
