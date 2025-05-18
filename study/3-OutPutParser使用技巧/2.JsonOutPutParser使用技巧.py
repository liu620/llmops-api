#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/18 15:46
@Author : liual
@File   : 2.JsonOutPutParser使用技巧.py
"""
import os

import dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class Joke(BaseModel):
    joke: str = Field(description="回答用户的冷笑话")
    punchline: str = Field(description="这个笑话的笑点")


dotenv.load_dotenv()
parser = JsonOutputParser(pydantic_object=Joke)

prompt = ChatPromptTemplate.from_template("""请根据用户提问的请求进行回答
{format_instructions}
{query}
""").partial(format_instructions=parser.get_format_instructions())

# print(prompt.format(query="请讲一个程序员的冷笑话"))

llm = ChatOpenAI(base_url=os.getenv("OPENAI_URL"), model="deepseek-reasoner")
joke = parser.invoke(llm.invoke(prompt.invoke({"query": "请讲一个程序员的冷笑话"})))
print(type(joke))
print(joke.get("punchline"))
print(joke)
