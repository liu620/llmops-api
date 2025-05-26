#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/22 11:32
@Author : liual
@File   : 1.对话消息历史组件基础.py
"""
from langchain_core.chat_history import InMemoryChatMessageHistory

chat_history = InMemoryChatMessageHistory()

chat_history.add_user_message("你好，我是刘大帅")
chat_history.add_ai_message("你好，我是deepseek, 有什么可以帮助你的么?")

print(chat_history)
