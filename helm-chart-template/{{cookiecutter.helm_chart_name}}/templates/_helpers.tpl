{% raw %}{{{% endraw %}/* vim: set filetype=mustache: */{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}/*
Expand the name of the chart.
*/{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- define "{{cookiecutter.helm_chart_name}}.name" -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- end -{% raw %}}}{% endraw %}

{% raw %}{{{% endraw %}/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- define "{{cookiecutter.helm_chart_name}}.fullname" -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- if .Values.fullnameOverride -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- else -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- $name := default .Chart.Name .Values.nameOverride -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- if contains $name .Release.Name -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- .Release.Name | trunc 63 | trimSuffix "-" -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- else -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- end -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- end -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- end -{% raw %}}}{% endraw %}

{% raw %}{{{% endraw %}/*
Create chart name and version as used by the chart label.
*/{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- define "{{cookiecutter.helm_chart_name}}.chart" -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- end -{% raw %}}}{% endraw %}

{% raw %}{{{% endraw %}/*
Common labels
*/{% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- define "{{cookiecutter.helm_chart_name}}.labels" -{% raw %}}}{% endraw %}
app.kubernetes.io/name: {% raw %}{{{% endraw %} include "{{cookiecutter.helm_chart_name}}.name" . {% raw %}}}{% endraw %}
helm.sh/chart: {% raw %}{{{% endraw %} include "{{cookiecutter.helm_chart_name}}.chart" . {% raw %}}}{% endraw %}
app.kubernetes.io/instance: {% raw %}{{{% endraw %} .Release.Name {% raw %}}}{% endraw %}
app.kubernetes.io/managed-by: {% raw %}{{{% endraw %} .Release.Service {% raw %}}}{% endraw %}
{% raw %}{{{% endraw %}- end -{% raw %}}}{% endraw %}
