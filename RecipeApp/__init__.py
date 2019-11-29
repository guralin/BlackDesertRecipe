from flask import Flask
from flask_cors import CORS

# static_folderとtemplate_folderについて
# https://qiita.com/mink0212/items/a4eb875f19b0e47718d3
#app = Flask(__name__, static_folder='RecipeApp/static', template_folder='RecipeApp/templates')
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins":"*"}})
# jsonのレスポンスに日本語が含まれていた場合にエスケープさせない
app.config['JSON_AS_ASCII'] = False

from RecipeApp import views
