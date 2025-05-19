#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/16 23:45
@Author : liual
@File   : app_handler
"""
import os
from dataclasses import dataclass
from uuid import UUID

from injector import inject
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from internal.schema.app_schema import CompletionReq
from internal.service.app_service import AppService
from pkg.response import success_json, validata_error_json, success_message


@inject
@dataclass
class AppHandler:
    app_service: AppService

    """应用控制器"""

    def create_app(self):
        """调用服务创建行的APP记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已经创建成功{app.id}");

    def get_app(self, id: UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用已经获取对应app的名字是{app.name}")

    def update_app(self, id: UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功修改, 修改的名字是{app.name}")

    def delete_app(self, id: UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，id为{app.id}")

    def debug(self, app_id: UUID):
        """聊天接口"""
        req = CompletionReq()
        if not req.validate():
            return validata_error_json(req.errors)

        prompt = ChatPromptTemplate.from_template("{query}")

        llm = ChatOpenAI(base_url=os.getenv("OPENAI_URL"), model="deepseek-chat")
        parser = StrOutputParser()
        chain = prompt | llm | parser

        return success_json(parser.invoke(chain.invoke({"query": req.query.data})))

    def ping(self):
        raise Exception("调用失败")
        # return {"ping": "pong"}
