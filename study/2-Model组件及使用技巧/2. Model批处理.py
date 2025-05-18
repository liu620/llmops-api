#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/18 14:40
@Author : liual
@File   : 2. Model批处理.py
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

ai_messages = llm.batch([
    chat_prompt.invoke({"query": "你好你是？"}),
    chat_prompt.invoke({"query": "请讲一个程序员的冷笑话"})
])

for ai_message in ai_messages:
    print(ai_message.content)
    print("====================")
