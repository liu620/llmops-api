#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/16 23:39
@Author : liual
@File   : test
"""
from injector import Injector, inject


class A:
    name: str = 'llmops'


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"Class A 的名字为 {self.a.name}")


injector = Injector()
b = injector.get(B)
b.print()
