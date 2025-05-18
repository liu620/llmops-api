#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/16 23:58
@Author : liual
@File   : http
"""
import logging
import os

from flask import Flask
from flask_migrate import Migrate

from config import Config
from internal.exception import CustomExcpetion
from internal.model import App
from internal.router import Router
from pkg.response import json, Response, HttpCode
from pkg.sqlalchemy import SQLAlchemy

logger = logging.getLogger(__name__)


class Http(Flask):
    """Http服务引擎"""

    def __init__(
            self,
            *args,
            config: Config,
            db: SQLAlchemy,
            migrate: Migrate,
            router: Router,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        # 注册应用类型
        self.config.from_object(config)
        self.register_error_handler(Exception, self._register_error_handler)

        db.init_app(self)
        migrate.init_app(self, db, directory="internal/migration")

        with self.app_context():
            _ = App()
            # db.create_all()
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        if isinstance(error, CustomExcpetion):
            return json(
                Response(
                    code=error.code,
                    message=error.message,
                    data=error.data
                )
            )
        if self.debug or os.getenv("FLASK_ENV") == "development":
            raise error
        return json(Response(
            code=HttpCode.FAIL,
            message=str(error),
            data={}
        ))
