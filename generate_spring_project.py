import json
import urllib

from cookiecutter.main import cookiecutter


def get_selection(param, json_output):
    return list(map(lambda json_obj: json_obj['id'], json_output[param]['values']))


response = urllib.request.urlopen("https://start.spring.io").read()
json_output = json.loads(response)
java_versions = get_selection('javaVersion', json_output)
java_versions.reverse()
languages = get_selection('language', json_output)
boot_versions = get_selection('bootVersion', json_output)

cookiecutter(
    'spring-boot-template',
    extra_context={'java_version': java_versions, 'app_language': languages, 'boot_version': boot_versions},
)
