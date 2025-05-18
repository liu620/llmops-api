#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/17 12:15
@Author : liual
@File   : exception
"""

from dataclasses import dataclass, field
from typing import Any

from pkg.response import HttpCode


@dataclass
class CustomExcpetion(Exception):
    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str, data: Any = None):
        super().__init__()
        self.message = message
        self.data = data


class FailException(CustomExcpetion):
    pass


class NotFoundException(CustomExcpetion):
    code: HttpCode = HttpCode.NOT_FOUND


class UnAuthorizedException(CustomExcpetion):
    code: HttpCode = HttpCode.UNAUTHORIZED


class ForBiddenException(CustomExcpetion):
    code: HttpCode = HttpCode.FORBIDDEN


class VaildateException(CustomExcpetion):
    code: HttpCode = HttpCode.VALIDATION_ERROR
