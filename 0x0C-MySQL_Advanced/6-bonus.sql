-- Create trigger to reset valid email
-- Is this the problem
DELIMETER $$
CREATE PROCEDURE AddBonus (
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT)
BEGIN
    INSERT INTO projects (name)
    SELECT project_name WHERE NOT EXISTS
    (SELECT * FROM projects WHERE name=project_name);
    SET @pro = (SELECT id FROM projects WHERE name=project_name);
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @pro, score);

END$$

DELIMETER ;
