FROM {{cookiecutter.docker_build_image_base}} as build-stage

WORKDIR /app
COPY ./{{cookiecutter.app_name}}/ /app/
RUN cd /app && {{cookiecutter.docker_app_build_command}}

# Create final image with nginx serving built files; the nginx-unprivileged variant is used
# as we must not run images in the context of the superuser. This image comes with user 'nginx' with UID 101 and
# runs as that user by default. The UID of this user is also used in runAsUser directive in the chart.
FROM nginxinc/nginx-unprivileged:1.17.2-alpine
COPY --from=build-stage /app/build/ /usr/share/nginx/html/
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
