#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/17 00:01
@Author : liual
@File   : app
"""
import dotenv
from flask_migrate import Migrate
from injector import Injector

from config import Config
from internal.router import Router
from internal.server import Http
from pkg.sqlalchemy import SQLAlchemy
from .module import ExtensionModule

dotenv.load_dotenv()
config = Config()

injector = Injector([ExtensionModule])
app = Http(__name__,
           config=config,
           db=injector.get(SQLAlchemy),
           migrate=injector.get(Migrate),
           router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
