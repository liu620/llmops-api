#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/22 12:45
@Author : liual
@File   : 2.文件对话消息历史组件实现记忆.py
"""
import dotenv
from langchain_community.chat_message_histories import FileChatMessageHistory
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(base_url="https://api.deepseek.com/v1")

chat_history = FileChatMessageHistory("./memory.txt")

while True:
    query = input('Human:')

    if query == 'q':
        break
    sys_prompt = (
        "你是deepseek机器人，可以根据上下文回复用户信息，上下文存放的是人类与你对话信息 \n\n"
        f"<context>{chat_history}</context>"
    )
    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=[
            {'role': 'system', "content": sys_prompt},
            {'role': 'user', 'content': query}
        ],
        stream=True
    )
    print("AI:", flush=True, end='')
    ai_message = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is None:
            break

        ai_message += content
        print(content, flush=True, end='')
    chat_history.add_user_message(query)
    chat_history.add_ai_message(ai_message)
    print('')
