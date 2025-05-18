#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/17 10:14
@Author : liual
@File   : config
"""
import os
from typing import Any

from .default_config import DEFAULT_CONFIG


def _get_env(key: str) -> Any:
    return os.environ.get(key, DEFAULT_CONFIG.get(key))


def _get_bool_env(key: str) -> Any:
    var: str = _get_env(key)
    return var.lower() == "true" if var is not None else False


class Config:
    def __init__(self):
        # 关闭CSRF保护
        self.WTF_CSRF_ENABLED = _get_bool_env("WTF_CSRF_ENABLE")
        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_DATABASE_OPTIONS = {
            "pool_size": _get_env("SQLALCHEMY_POOL_SIZE"),
            "pool_recycle": _get_env("SQLALCHEMY_POOL_RECYCLE")
        }
        self.SQLALCHEMY_ECHO = _get_bool_env("SQLALCHEMY_ECHO")
