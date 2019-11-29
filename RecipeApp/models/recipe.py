#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

from RecipeApp.models.setting import session
from RecipeApp.models.init import Recipe, Item, Category

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

    show = []
    for row in items:
        show.append(row.name)
    
    return show


def item_name_to_id(name):
    match_list = session.query(Item).filter(Item.name==name).all()
    if len(match_list) == 1:
        return match_list[0].item_id
    else:
        raise ValueError("該当するidが存在しません")

def id_to_item_name(item_id):
    match_list = session.query(Item).filter(Item.item_id==item_id).all()
    if len(match_list) == 1:
        return match_list[0].name
    else:
        raise ValueError("該当するidが存在しません")

def add_item_when_dont_exist(name):
    match_count = session.query(Item).filter(Item.name==name).count() 
    if match_count == 0:
        add_item(name)

def import_item_for_csv(path):
    with open(path,"r",encoding="shift-jis") as f:
        cin = csv.reader(f)
        villains = [row for row in cin]
        for row in villains:
            add_item_when_dont_exist(row[2])
            add_item_when_dont_exist(row[3])

def category_name_to_id(category_name):
    match_list = session.query(Category).filter(Category.category_name==category_name).all()
    if len(match_list) == 1:
        return match_list[0].category_id
    else:
        raise ValueError("該当するカテゴリーが存在しません")

def add_category(category_name):
    category = Category()
    category.category_name = category_name
    session.add(category)
    session.commit()

def add_recipe(category, finished_item, material, material_count):
    recipe = Recipe()
    recipe.category_id = category_name_to_id(category)
    recipe.finished_item_id = item_name_to_id(finished_item)
    recipe.material_id = item_name_to_id(material)
    recipe.material_count = material_count

    session.add(recipe)
    session.commit()

def show_matching_recipe(recipe_name):
    material_list = []
    finished_item_id = item_name_to_id(recipe_name)
    match_material = session.query(Recipe).filter(Recipe.finished_item_id==finished_item_id).all() 
    for row in match_material:
        name = id_to_item_name(row.material_id)
        count = row.material_count
        material_list.append({"name":name, "count":count})
    return material_list
        
        
    
    
def import_recipe_for_csv(path):
    with open(path,"r",encoding="shift-jis") as f:
        cin = csv.reader(f)
        villains = [row for row in cin]
        for row in villains:
            add_recipe(row[1],row[2],row[3],row[4])
