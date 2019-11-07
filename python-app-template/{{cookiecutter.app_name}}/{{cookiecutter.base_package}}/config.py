#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2007-2019, GoodData(R) Corporation. All rights reserved
import json
import os
from pathlib import Path
from typing import Dict

import yaml


def _merge_dict(origin: Dict, update: Dict) -> Dict:
    """
    Takes original dictionary and updates it with items from second parameter. This methods performs deep merge.

    :param origin: dictionary to be updated
    :param update: dictionary with new values
    :return: original dictionary updated with values from the update parameter
    """
    for key in update:
        if key in origin:
            if isinstance(origin[key], dict) and isinstance(update[key], dict):
                _merge_dict(origin[key], update[key])
            else:
                origin[key] = update[key]
        else:
            origin[key] = update[key]
    return origin


class Config:
    """
    Class holding configuration of the whole app.
    """

    def __init__(self, config: Dict) -> None:
        """
        Initializes new instance with provided config.

        :param config: config to be used
        """
        self._config = config

    @staticmethod
    def load(path: Path = Path(__file__).parent / 'config.yaml'):
        """
        Loads config from provided path and merges it with config defined in `APPLICATION_JSON` environment variable.

        :param path: location of the config file, defaults to one on classpath
        :return: loaded config
        :rtype: Config
        """
        with path.open() as f:
            config = yaml.safe_load(f)

        env_config = json.loads(os.getenv('APPLICATION_JSON', '{}'))
        config = _merge_dict(config, env_config)

        return Config(config)

    @property
    def logging(self) -> Dict:
        """
        Returns configuration for logging.

        :return: logging configuration
        """
        return self._config.get('logging', {})

    @property
    def probe_enabled(self):
        """
        Returns whether kubernetes probe endpoint is enabled.

        :return: true if probe endpoint is enabled
        """
        return self._config.get('probe_enabled', True)

    @property
    def interval(self) -> int:
        """
        Returns app cycle interval.

        :return: synchronization interval
        """
        return self._config.get('interval', 10)
