#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2007-2019, GoodData(R) Corporation. All rights reserved
import os
from pathlib import Path

from {{cookiecutter.base_package}}.config import Config


def test_logging_config():
    try:
        os.environ['APPLICATION_JSON'] = \
            '{"logging": {"version": 1, "handlers": {"syslog": {"address": ["127.0.0.1", 5140]}}}}'
        path = Path(__file__).parent / 'simple-config.yaml'

        config = Config.load(path=path)
        assert config.logging['handlers']['syslog']['address'] == ['127.0.0.1', 5140]
        assert config.logging['handlers']['syslog']['facility'] == 'local5'
        assert config.logging['root'] == {'handlers': ['console'], 'level': 'INFO'}
    finally:
        del os.environ['APPLICATION_JSON']


def test_env_logging_config():
    try:
        os.environ['APPLICATION_JSON'] = \
            '{"logging": {"version": 1, "handlers": {"syslog": {"class": "logging.handlers.SysLogHandler", ' \
            '"formatter": "syslog", "facility": "local4", "address": ["127.0.0.1", 5140]}}, ' \
            '"root": {"handlers": ["syslog"]}}}'
        path = Path(__file__).parent / 'simple-config.yaml'

        config = Config.load(path=path)

        assert config.logging['formatters'].get('syslog') is not None
        assert config.logging['handlers']['syslog'].get('formatter') is not None
        assert config.logging['handlers']['syslog'] == {
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'syslog',
            'facility': 'local4',
            'address': ['127.0.0.1', 5140]
        }
        assert config.logging['root'] == {'handlers': ['syslog'], 'level': 'INFO'}
    finally:
        del os.environ['APPLICATION_JSON']
