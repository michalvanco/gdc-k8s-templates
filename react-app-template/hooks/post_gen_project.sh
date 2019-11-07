#!/usr/bin/env bash

echo "Generating JS project using 'npx create-react-app'"

if [ "{{cookiecutter.js_vs_typescript}}" == "ts" ]; then
  echo "Typescript option is enabled"
  options+="--typescript"
fi

npx create-react-app {{cookiecutter.app_name}} $options
