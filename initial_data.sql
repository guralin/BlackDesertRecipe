CREATE TABLE item (                                                                                  
        item_id INTEGER NOT NULL,                                                                    
        name VARCHAR(128) NOT NULL,                                                                  
        detail VARCHAR(512),                                                                         
        "NPC_price" INTEGER,                                                                         
        exchange_price INTEGER,                                                                      
        PRIMARY KEY (item_id),                                                                       
        UNIQUE (name)                                                                                
) CREATE TABLE recipe (
        recipe_id INTEGER NOT NULL,
        category_id INTEGER NOT NULL,
        finished_item_id INTEGER NOT NULL,
        material_id INTEGER NOT NULL,
        material_count INTEGER NOT NULL,
        PRIMARY KEY (recipe_id)
)
CREATE TABLE category (
        category_id SERIAL NOT NULL,
        category_name VARCHAR(128) NOT NULL,
        PRIMARY KEY (category_id)
)
