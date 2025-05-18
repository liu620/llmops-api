#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/18 17:12
@Author : liual
@File   : 2.LCEL表达式简化版本.py
"""
import os

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(base_url=os.getenv("OPENAI_URL"), model="deepseek-reasoner")
parser = StrOutputParser()

chain = prompt | llm | parser

ai_message = chain.invoke({"query": "请讲一个程序员的冷笑话"})

for output in ai_message:
    print(output, flush=True, end="")
