#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/18 14:41
@Author : liual
@File   : 3. Model流式输出.py
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

response = llm.stream(chat_prompt.invoke({"query": "你能简单介绍一下LLM和LLMOps么"}))

for chunk in response:
    print(chunk.content, flush=True, end="")
