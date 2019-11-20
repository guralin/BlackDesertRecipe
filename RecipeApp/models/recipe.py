#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setting import session

from init import Recipe, Item

def add_item(item_name, detail="", NPC_price=0, exchange_price=0):
    item = Item()

    item.name = item_name
    item.detail = detail
    item.NPC_price = NPC_price
    item.exchange_price = exchange_price

    session.add(item)
    session.commit()

def show_item():
    items = session.query(Item).all()
    for item in items:
        print(item)
