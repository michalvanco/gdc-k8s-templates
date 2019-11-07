# Template for common k8s helm chart

* incl. deployment, service, monitoring rules etc.

## Requirements
 * `cookiecutter`

## Example usage
```
$ cookiecutter helm-chart-template
helm_chart_name [test-app]: datawarehouse-restapi
docker_image_name [datawarehouse-restapi]: 
docker_application_port [8080]: 
docker_user_id [1111]: 1112
k8s_values_first_level [default]: datawarehouse
k8s_values_second_level [testApp]: restapi
k8s_service_name [datawarehouse-restapi]: 
```

See the generated structure under `datawarehouse-restapi` directory.
