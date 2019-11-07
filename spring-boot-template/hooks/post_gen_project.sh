#!/usr/bin/env bash

echo "Generating project using the start.spring.io tooling"

curl https://start.spring.io/starter.zip -o {{cookiecutter.app_name}}.zip \
-d 'groupId={{cookiecutter.group_id}}' \
-d 'artifactId={{cookiecutter.artifact_id}}' \
-d 'name={{cookiecutter.app_name}}' \
-d 'description={{cookiecutter.description}}' \
-d 'packageName={{cookiecutter.package_name}}' \
-d 'dependencies={{cookiecutter.dependencies}}' \
-d 'javaVersion={{cookiecutter.java_version}}' \
-d 'language={{cookiecutter.app_language}}' \
-d 'type={{cookiecutter.build_system}}-project' \
-d 'packaging=jar'

unzip {{cookiecutter.app_name}}.zip

rm {{cookiecutter.app_name}}.zip


