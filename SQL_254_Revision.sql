USE db_zootes2
GO

/*Retrieve all names within the species_name column using the alias 
"Species Name:" from the species table and their corresponding 
nutrition_type under the alias "Nutrition Type:" from the
nutrition table.*/


SELECT * FROM tbl_species;
SELECT * FROM tbl_nutrition;

SELECT tbl_species.species_name AS [Species Name], tbl_nutrition.nutrition_type AS [Nutrition Type]
FROM tbl_species
INNER JOIN  tbl_nutrition ON species_nutrition = nutrition_type;