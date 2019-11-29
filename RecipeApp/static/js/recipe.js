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
        information.style.color = 'red';
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
        
        //output_data.textContent = JSON.stringify(recipeName);
        
        let recipe_list = [];

        for(row in recipeName["material"]){
            
            recipe_list.push(recipeName["material"][row]["name"] + ":" + recipeName["material"][row]["count"]);
        }
        console.log(recipe_list);
        output_data.textContent = recipe_list;
        information.textContent = recipeName["finished_item"];

    }
        
}
