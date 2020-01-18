CREATE TABLE aoe."Structures"
(order_id         integer PRIMARY KEY, 
age               name,
armor             name,
attack           float,
build_time         integer,
cost              name,
expansion         name,
hit_points         integer,
id                 integer,
line_of_sight    float,
name              name,
range             name,
reload_time      float,
special           name
)

WITH (
    OIDS = FALSE
);

ALTER TABLE aoe."Structures"
    OWNER to postgres;