# BlackDesertRecipe
MMORPGのアイテムのレシピを再帰的に表示することが出来るWebアプリケーション

## 導入
1. sudo -u postgres -i
1. psql
1. `CREATE DATABASE black_desert_recipe OWNER=guralin TEMPLATE = template0 ENCODING='UTF8' LC_COLLATE='C' LC_CTYPE='C';`

1. psqlとpostgresユーザーから抜ける

1. cd ~/BlackDesertRecipe 

1. source blackdesertenv/bin/activate

1. python 

1. `from RecipeApp.models import init,recipe`
`init.main(" ")`
`recipe.set_category("料理")`
`recipe.set_category("錬金")`
`recipe.import_item_for_csv("recipe_data.csv")`
`recipe.import_recipe_for_csv("recipe_data.csv")`

デプロイ方法についてはこちらを見てください
[flask を uWSGI と Nginx でデプロイする](https://qiita.com/ekzemplaro/items/a570f79de254428a151d)

## TODO
- Ansibleを使用して簡単にデプロイできるようにする。

## URL
[公式ページ](relazy.work)
