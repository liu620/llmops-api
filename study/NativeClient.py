#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/22 17:37
@Author : liual
@File   : NativeClient.py
"""
import os

import dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(base_url="https://api.deepseek.com/v1")

llm = ChatOpenAI(base_url=os.getenv("OPENAI_URL"), model="deepseek-chat")
