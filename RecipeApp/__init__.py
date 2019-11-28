from flask import Flask


app = Flask(__name__)
# jsonのレスポンスに日本語が含まれていた場合にエスケープさせない
app.config['JSON_AS_ASCII'] = False

from RecipeApp import views
