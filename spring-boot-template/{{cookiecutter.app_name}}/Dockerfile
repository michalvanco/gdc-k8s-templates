FROM harbor.intgdc.com/tools/gdc-java-{{cookiecutter.java_version.split('.')[-1]}}-jdk:latest as builder

WORKDIR /{{cookiecutter.app_name}}

ARG JAR_FILE=target/{{cookiecutter.app_name}}-1.0.0-SNAPSHOT.jar
COPY ${JAR_FILE} ./{{cookiecutter.app_name}}.jar

RUN set -x \
    && mkdir -p dependency \
    && cd dependency \
    && jar -xf ../*.jar \
    && true

FROM harbor.intgdc.com/tools/gdc-java-{{cookiecutter.java_version.split('.')[-1]}}-jre:latest

LABEL image_name="{{cookiecutter.docker_image_name}}"
LABEL maintainer="{{cookiecutter.team}} <{{cookiecutter.team}}@gooddata.com>"
LABEL git_repository_url="{{cookiecutter.target_github_repository}}"
LABEL parent_image="harbor.intgdc.com/tools/gdc-java-{{cookiecutter.java_version.split('.')[-1]}}-jre:latest"

RUN groupadd -g {{cookiecutter.docker_user_id}} {{cookiecutter.app_name}} && \
    useradd -r -u {{cookiecutter.docker_user_id}} -g {{cookiecutter.app_name}} {{cookiecutter.app_name}}
USER {{cookiecutter.app_name}}

VOLUME /tmp
ENV SPRING_PROFILES_ACTIVE="k8s"

WORKDIR /{{cookiecutter.app_name}}

ENTRYPOINT exec java -Djava.security.egd=file:/dev/./urandom $JAVA_OPTS -cp /{{cookiecutter.app_name}}:/{{cookiecutter.app_name}}/lib/* \
    {{cookiecutter.package_name}}.{{cookiecutter.app_name.replace('-', ' ').title().replace(' ','')}}Application

COPY --from=builder /{{cookiecutter.app_name}}/dependency/BOOT-INF/lib lib
COPY --from=builder /{{cookiecutter.app_name}}/dependency/META-INF META-INF
COPY --from=builder /{{cookiecutter.app_name}}/dependency/BOOT-INF/classes .

ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT
