#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/17 11:12
@Author : liual
@File   : response
"""
from dataclasses import dataclass, field
from typing import Any

from flask import jsonify

from .http_code import HttpCode


@dataclass
class Response:
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json(data: Response) -> tuple[Response, int]:
    return jsonify(data), 200


def success_json(data: Any) -> tuple[Response, int]:
    return json(Response(HttpCode.SUCCESS, message="", data=data))


def fail_json(data: Any):
    return json(Response(HttpCode.FAIL, message="", data=data))


def validata_error_json(errors: dict = None):
    first = next(iter(errors))
    if first is not None:
        msg = errors.get(first)[0]
    else:
        msg = ""
    return json(Response(code=HttpCode.VALIDATION_ERROR, message=msg, data=errors))


def message(code: HttpCode, msg: str):
    return jsonify(Response(code=code, message=msg, data={}))


def success_message(msg: str):
    return message(code=HttpCode.SUCCESS, msg=msg)


def fail_message(msg: str):
    return message(code=HttpCode.FAIL, msg=msg)


def not_found_message(msg: str):
    return message(code=HttpCode.NOT_FOUND, msg=msg)


def unauthorized_message(msg: str):
    return message(code=HttpCode.UNAUTHORIZED, msg=msg)


def forbidden_message(msg: str):
    return message(code=HttpCode.FORBIDDEN, msg=msg)
