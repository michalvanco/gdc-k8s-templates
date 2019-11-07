#!/usr/bin/env bash

echo "Generating React project using 'npx create-react-app'..."

if [ "{{cookiecutter.js_vs_typescript}}" == "ts" ]; then
  echo "--typescript option is enabled"
  options+="--typescript"
fi

npx create-react-app {{cookiecutter.app_name}} $options
