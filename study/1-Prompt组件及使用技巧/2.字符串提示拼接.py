#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/18 13:09
@Author : liual
@File   : 2.字符串提示拼接.py
"""

from langchain_core.prompts import PromptTemplate

prompt = (
        PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
        + ", 让我开心一下"
        + "\n 哈哈哈哈{xixi}"
)
print(prompt)
