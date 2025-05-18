#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/18 15:30
@Author : liual
@File   : 1.StrOutPutParser使用技巧.py
"""
import os

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

llm = ChatOpenAI(base_url=os.getenv("OPENAI_URL"), model="deepseek-reasoner")

# ChatPromptTemplate.from_messages();
str_parser = StrOutputParser()
str = str_parser.invoke("AAAAAAAA")
print(str)
