#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 参考URL: https://qiita.com/ckern/items/a762b1bc0f192a55eae8

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# local環境用
DATABASE = 'postgresql://{user_name}:{password}@{host_ip}/{db_name}'.format(user_name="guralin", password="test", host_ip="localhost", db_name="black_desert_recipe")

ENGINE = create_engine(
        DATABASE,
        encoding = "utf-8",
        echo=True
)

# sessionの作成
session = scoped_session(
        sessionmaker(
            autocommit = False,
            autoflush = False,
            bind = ENGINE
        )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()
