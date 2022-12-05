DO $$
DECLARE
    new_manufacture_name cars.manufacture_name%TYPE;
    new_model_name cars.model_name%TYPE;

BEGIN
	new_manufacture_name := 'company';
	new_model_name := 'model';

    FOR counter IN 1..7
        LOOP
            INSERT INTO cars 
			VALUES (10+counter, new_manufacture_name || (counter + 10), new_model_name || (counter + 10), (SELECT CAST(RANDOM()*(10-1)+1 AS INT)));
        END LOOP;
END
$$

SELECT * FROM cars; 