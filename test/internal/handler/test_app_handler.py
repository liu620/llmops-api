#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/17 13:40
@Author : liual
@File   : text_app_handler
"""
import pytest

from pkg.response import HttpCode


class TestAppHandler:
    @pytest.mark.parametrize("query", ["你好", None])
    def test_completion(self, query, client) -> None:
        response = client.post("/app/completion", json={"query": query})
        assert response.status_code == 200
        if query is None:
            assert response.json.get("code") == HttpCode.VALIDATION_ERROR
        else:
            assert response.json.get("code") == HttpCode.SUCCESS
