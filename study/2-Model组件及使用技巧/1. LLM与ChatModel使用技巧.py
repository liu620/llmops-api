#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/18 14:20
@Author : liual
@File   : 1. LLM与ChatModel使用技巧.py
"""
import os
from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是深度求索开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}"),
]).partial(now=datetime.now)

llm = ChatOpenAI(base_url=os.getenv("OPENAI_URL"), model="deepseek-reasoner")
ai_messages = llm.invoke(chat_prompt.invoke({"query": "现在是几点，请讲一个程序员的冷笑话"}))
print(ai_messages.type)
print(ai_messages.content)
print(ai_messages.response_metadata)
