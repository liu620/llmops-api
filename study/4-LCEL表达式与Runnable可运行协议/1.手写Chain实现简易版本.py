#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/18 17:00
@Author : liual
@File   : 1.手写Chain实现简易版本.py
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


class Chain:
    steps: list = []

    def __init__(self, steps: list):
        self.steps = steps

    def invoke(self, input: Any) -> Any:
        for step in self.steps:
            input = step.invoke(input)
            print("步骤：", step)
            print("输出：", input)
        return input


# chain = prompt | llm | parser

chain = Chain(steps=[prompt, llm, parser])
print(chain.invoke({"query": "你好，你是？"}))
