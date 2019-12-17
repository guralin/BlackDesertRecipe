function updateRecipe(){
    let information = document.getElementById('info');
    information.textContent = "Now Loading....";
    let requestURL = 'http://localhost:5000/api';
    let request = new XMLHttpRequest();
    request.open('POST', requestURL);
    request.setRequestHeader('Content-Type', 'application/json');
    request.responseType = 'json';
    request.onerror = function(){
        information.textContent = "Connection Error!!";
    }
    
    request.onload =  function(){
        let recipeStatus = request.response;
        fetchRecipe(recipeStatus);
    }

    let input_data = document.getElementById("input_finished_item").value;
    request.send('{"finished_item":"' + input_data + '"}');
    return false;
    function fetchRecipe(recipeName){
        let output_data = document.getElementById("recipe");
        console.log(recipeName);
        
        let recipe_list = "<table border=1>"+
            "<tr><th>name</th><th>個数</th></tr>";

        for(row in recipeName["material"]){
            
            recipe_list += "<tr><td>" + recipeName["material"][row]["name"] + "</td><td>" + recipeName["material"][row]["count"] + '</td></tr>';
        }
        console.log(recipe_list);

        recipe_list += "</table>"
        
        // レシピのテーブルを結合することで履歴が残るような挙動になった。
        // ほしい挙動ではあったけど、意図した挙動ではない
        output_data.innerHTML = recipe_list;
        information.textContent = "料理名 : " + recipeName["finished_item"];

    }
}
