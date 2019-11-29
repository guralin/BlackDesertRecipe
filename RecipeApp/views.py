#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import make_response, jsonify, request

from RecipeApp import app
from RecipeApp.models import recipe

@app.route('/', methods=['POST'])
def show_recipe_material():
    request_body = request.json
    response = {}
    finished_item = request_body.get("finished_item")
    response["finished_item"] = finished_item
    response["material"] = recipe.show_matching_recipe(finished_item)

    return make_response(jsonify(response))
    
