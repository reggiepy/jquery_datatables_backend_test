# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2023/2/17 13:37

from typing import Union

import six
import uvicorn

from datatables_backend import settings, common
from api.router import api_router

app = common.init_app(api_router)


class Application:
    def __init__(
            self,
            gconfig: Union[dict, None] = None,
            **options
    ):
        self.gconfig = gconfig
        self.uvicorn_kwargs = self._default_uvicorn_kwargs
        self.config = self.configure(self.gconfig, **options)

    def configure(self, gconfig: Union[dict, None] = None, prefix='agent_gateway.', **options):
        """
        configure
        :param dict gconfig: a "global" configuration dictionary whose values can be overridden by
            keyword arguments to this method
        :param str prefix: prefix
        :param options: other config
        :return:
        """
        gconfig = gconfig or {}

        # If a non-empty prefix was given, strip it from the keys in the
        # global configuration dict
        if prefix:
            prefixlen = len(prefix)
            gconfig = dict((key[prefixlen:], value) for key, value in six.iteritems(gconfig)
                           if key.startswith(prefix))

        config = {}
        for k, v in gconfig.items():
            config[k] = v
        # Override any options with explicit keyword arguments
        config.update(options)

        self._configure(config)
        return config

    def _configure(self, config):
        if config.get("host"):
            self.uvicorn_kwargs["host"] = config.get("host")
        if config.get("port"):
            self.uvicorn_kwargs["port"] = config.get("port")
        if config.get("reload"):
            self.uvicorn_kwargs["reload"] = config.get("reload")
        if config.get("workers"):
            self.uvicorn_kwargs["workers"] = config.get("workers")
        if config.get("log_config"):
            self.uvicorn_kwargs["log_config"] = config.get("log_config")

    @property
    def _default_uvicorn_kwargs(self):
        return {
            "host": settings.HOST,
            "port": settings.PORT,
            "workers": settings.WORKERS,
            "reload": settings.DEBUG,
            "log_config": settings.LOG_CONFIG,
        }

    def run(self):
        uvicorn.run(
            app=app,
            **self.uvicorn_kwargs
        )


if __name__ == '__main__':
    Application().run()
