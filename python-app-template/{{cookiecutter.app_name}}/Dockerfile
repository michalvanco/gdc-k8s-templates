FROM harbor.intgdc.com/tools/gdc-python-3.6 as builder

WORKDIR /{{cookiecutter.app_name}}

COPY setup.py setup.py
COPY MANIFEST.in MANIFEST.in
ADD {{cookiecutter.base_package}} {{cookiecutter.base_package}}

RUN python3.6 setup.py sdist

FROM harbor.intgdc.com/tools/gdc-python-3.6

LABEL image_name="{{cookiecutter.app_name}}"
LABEL maintainer="{{cookiecutter.maintainer}}"
LABEL git_repository_url="{{cookiecutter.target_github_repository}}"
LABEL parent_image="harbor.intgdc.com/tools/gdc-python-3.6"

WORKDIR /{{cookiecutter.app_name}}

RUN groupadd -g 1112 {{cookiecutter.app_name}} && \
    useradd -r -u 1112 -g {{cookiecutter.app_name}} {{cookiecutter.app_name}}

ENTRYPOINT [ "python3.6", "/usr/local/bin/{{cookiecutter.app_name}}" ]

COPY requirements.txt .
RUN pip3.6 install -r requirements.txt
COPY --from=builder /{{cookiecutter.app_name}}/dist/{{cookiecutter.app_name}}-1.0.0.tar.gz .
RUN pip3.6 install {{cookiecutter.app_name}}-1.0.0.tar.gz

USER {{cookiecutter.app_name}}

ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT
