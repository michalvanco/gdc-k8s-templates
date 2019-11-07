#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2007-2019, GoodData(R) Corporation. All rights reserved
import logging.config
import signal
import threading
import time
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict

import prometheus_client

from {{cookiecutter.base_package}}.config import Config

logger = logging.getLogger(__name__)

_REQUEST_TIME = prometheus_client.Summary('http_server_requests_seconds', 'Time spent processing request',
                                          ['method', 'status', 'uri'])

_app = None


def _setup_logging(default_level: int = logging.DEBUG, config: Dict = None):
    """
    Sets up logging configuration.

    :param default_level: default logging level used for basic configuration
    :param config: config used for dictionary configuration
    """
    if config:
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


class ProbeHandler(BaseHTTPRequestHandler):
    """
    HTTP handler for k8s probe requests.
    """

    def __init__(self, *args) -> None:
        """
        Initializes new instance.

        :param args: args for the super class initialization
        """
        # this needs to be last call
        super().__init__(*args)

    def log_message(self, format, *args):
        logger.info(format, *args)

    def do_GET(self):
        start_time = time.time()
        try:
            # TODO fill some basic probes here
            self.send_response(HTTPStatus.NO_CONTENT)
            self.end_headers()
            self._observe(HTTPStatus.NO_CONTENT, start_time)
        except Exception:
            logger.exception('Error encountered during probe call')
            self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR)
            self._observe(HTTPStatus.INTERNAL_SERVER_ERROR, start_time)

    def _observe(self, code, start_time):
        _REQUEST_TIME.labels('GET', code.value, self.path).observe(time.time() - start_time)


class App:
    """
    Main executor object responsible for app logic.
    """

    def __init__(self, config: Config, stop_event: threading.Event = threading.Event()) -> None:
        """
        Initializes new instance.

        :param config: config
        """
        self._config = config
        if config.probe_enabled:
            self._server = HTTPServer(('', 8080),
                                      lambda *args: ProbeHandler(*args))
            threading.Thread(target=lambda: self._server.serve_forever(), name='ProbeThread', daemon=True).start()
        else:
            self._server = None
        self._stop_event = stop_event

    def run(self) -> None:
        """
        Runs infinite loop.
        """
        while not self._stop_event.is_set():
            try:
                # TODO add loop logic
                logger.info('Hello, world!')
            except Exception:
                logger.exception('Exception encountered during synchronization cycle.')
            finally:
                self._stop_event.wait(self._config.interval)
        if self._server:
            self._server.socket.close()

    def stop(self) -> None:
        self._stop_event.set()


def _signal_handler(signum, frame):
    global _app
    if _app:
        logger.info('Signal %s sent. Setting stop flag to stop execution', signum)
        _app.stop()


def main():
    # Set handler for SIGINT and SIGTERM signals to stop the execution loop
    signal.signal(signal.SIGINT, _signal_handler)
    signal.signal(signal.SIGTERM, _signal_handler)

    _setup_logging()
    logger.info("Let's get this party started...")

    logger.debug('action=load_configuration status=start')
    config = Config.load()
    logger.info('action=load_configuration status=finished')

    logger.debug('action=update_logging_config status=start')
    _setup_logging(config=config.logging)
    logger.info('action=update_logging_config status=finished')

    prometheus_client.start_http_server(8000)

    global _app
    _app = App(config)
    _app.run()
    logger.info('...and we are done!')


if __name__ == '__main__':
    main()
