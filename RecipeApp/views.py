#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import make_response, jsonify, request

from RecipeApp import app
from RecipeApp.models import recipe

@app.route('/')
def index():
    return str(recipe.show_item())
