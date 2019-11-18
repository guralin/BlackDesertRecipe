CREATE TABLE item(
    id serial primary key,
    name varchar(128) NOT NULL,
    detail varchar(512),
    NPC_price int,
    exchange_price int
);

CREATE TABLE category(
    category_id int,
    category_name varchar(128)
);
CREATE TABLE recipe(
    recipe_id  serial primary key,
    category_id int,
    finished_item int,
    material1 int,
    material2 int,
    material3 int,
    material4 int,
    material5 int,
    material6 int
);
