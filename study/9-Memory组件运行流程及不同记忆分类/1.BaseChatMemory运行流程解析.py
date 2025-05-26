#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/22 16:53
@Author : liual
@File   : 1.BaseChatMemory运行流程解析.py
"""
import dotenv

from langchain.memory.chat_memory import BaseChatMemory

# 加载文件配置信息
dotenv.load_dotenv()

memory = BaseChatMemory(
    input_key="query",
    output_key="output",
    return_message=True,

)

memory_variable = memory.load_memory_variables({})
