# Template for React UI application

 * incl. multi-stage Dockerfile, helm chart, nginx configuration, jenkins-ii configuration
 * `.js` or `.ts` are supported

## Requirements
 * `cookiecutter`
 * `npx` (+ `npm`)

## Example usage
```
$ cookiecutter react-app-template
app_name [test-app]: dashboards-ui
Select js_vs_typescript:
1 - js
2 - ts
Choose from 1, 2 (1, 2) [1]: 2
docker_image_name [dashboards-ui]: 
docker_build_image_base [node:10-alpine]: 
docker_app_build_command [npm install && npm run build]: 
docker_final_image_base [nginxinc/nginx-unprivileged:1.17.2-alpine]: 
docker_application_port [8080]: 
docker_user_id [1111]: 101
helm_chart_name [dashboards-ui]: 
k8s_values_first_level [client]: 
k8s_values_second_level [testApp]: dashboardsUi
k8s_service_name [dashboards-ui]: 
Generating JS project using 'npx create-react-app'
Typescript option is enabled
...
```

See the generated structure under `dashboards-ui` directory.

Details how to build / run application locally or deploy it in k8s is in generated
README file.
