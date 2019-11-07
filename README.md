# Quick & easy bootstrapping of k8s microservices

This "Hackathon" project aims to provide a support for bootstrapping new microservices
which should be developed by us (ideally locally) and deployed in k8s.

## Requirements
 * install `cookiecutter` tool with `$ brew install cookiecutter` or `$ pip install cookiecutter`

## Documentation
 * https://cookiecutter.readthedocs.io
 * https://github.com/cookiecutter/cookiecutter

## Supported GoodData templates
 * [common Helm chart](./helm-chart-template)
 * [React Application](./react-app-template)
 * [Spring Boot Application](./spring-boot-template)


## How to generate new service
```
$ git clone git@github.com:michalvanco/gdc-k8s-templates.git
$ cd gdc-k8s-templates
$ cookiecutter <template-dir> -o <output-dir>
```
You will be prompted for all required variables and generated directory structure will be produced
in `<output-dir>`. 

## Limitations
 * to eliminate the duplication of the similar files (jenkins-ii config, helm charts, etc.) we
 would like to use symlinks but there is currently an issue and it does not
 render the content of symlinked directories, see [github issue](https://github.com/cookiecutter/cookiecutter/issues/865)

## Hackathon developers
 * [Michal Vanco](https://github.com/michalvanco)
 * [Matej Plch](https://github.com/matejuh)
