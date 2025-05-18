#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/17 14:00
@Author : liual
@File   : conftest
"""
import pytest

from app.http.app import app


@pytest.fixture
def client():
    """测试客户端 fixture"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
