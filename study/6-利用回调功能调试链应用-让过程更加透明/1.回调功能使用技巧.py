#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/18 19:52
@Author : liual
@File   : 1.回调功能使用技巧.py
"""

import os
import time
from typing import Any, Optional, Union
from uuid import UUID

import dotenv
from langchain import ChatOpenAI
from langchain_core.callbacks import StdOutCallbackHandler, BaseCallbackHandler
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.outputs import GenerationChunk, ChatGenerationChunk, LLMResult
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

dotenv.load_dotenv()


class LLMOpsCallbackHandler(BaseCallbackHandler):
    start_at: float = 0
    end_at: float = 0

    def on_chat_model_start(
            self,
            serialized: dict[str, Any],
            messages: list[list[BaseMessage]],
            *,
            run_id: UUID,
            parent_run_id: Optional[UUID] = None,
            tags: Optional[list[str]] = None,
            metadata: Optional[dict[str, Any]] = None,
            **kwargs: Any,
    ) -> Any:
        print("聊天模型开始执行了")
        print("serialized: ", serialized)
        print("messages: ", messages)

    def on_llm_new_token(
            self,
            token: str,
            *,
            chunk: Optional[Union[GenerationChunk, ChatGenerationChunk]] = None,
            run_id: UUID,
            parent_run_id: Optional[UUID] = None,
            **kwargs: Any,
    ) -> Any:
        print("token 生成了")
        print("token: ", token)

    def on_llm_start(
            self,
            serialized: dict[str, Any],
            prompts: list[str],
            *,
            run_id: UUID,
            parent_run_id: Optional[UUID] = None,
            tags: Optional[list[str]] = None,
            metadata: Optional[dict[str, Any]] = None,
            **kwargs: Any,
    ) -> Any:
        self.start_at = time.time()

    def on_llm_end(
            self,
            response: LLMResult,
            *,
            run_id: UUID,
            parent_run_id: Optional[UUID] = None,
            **kwargs: Any,
    ) -> Any:
        self.end_at = time.time()
        print(f"llm返回了，共记：{self.end_at - self.start_at}")


prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(base_url=os.getenv("OPENAI_URL"), model="deepseek-chat")
parser = StrOutputParser()

chain = {
            "query": RunnablePassthrough()
        } | prompt | llm | parser

ai_message = chain.invoke("你好，你是谁?", config={"callbacks": [StdOutCallbackHandler(), LLMOpsCallbackHandler()]})

print(ai_message)
