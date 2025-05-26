#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/22 17:30
@Author : liual
@File   : 1.缓冲窗孔记忆示例.py
"""
import os
from operator import itemgetter

import dotenv
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
llm = ChatOpenAI(base_url=os.getenv("OPENAI_URL"), model="deepseek-chat")

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是deepseek开发的聊天机器人，请根据对应的上下文回复用户问题"),
    MessagesPlaceholder("history"),
    ("human", "{query}")
])

memory = ConversationBufferWindowMemory(
    k=2,
    return_messages=True,
    input_key="query",
)

chain = RunnablePassthrough.assign(
    history=RunnableLambda(memory.load_memory_variables) | itemgetter("history"),
) | prompt | llm | StrOutputParser()

while True:
    query = input("Human:")

    if query == "q":
        exit(0)

    chain_input = {"query": query, "history": []}
    response = chain.stream(chain_input)
    print("AI:", flush=True, end="")
    out_put = ""
    for chunk in response:
        out_put += chunk
        print(chunk, flush=True, end="")
    memory.save_context(chain_input, {"output": out_put})
    print("")
    print("history: ", memory.load_memory_variables({}))
