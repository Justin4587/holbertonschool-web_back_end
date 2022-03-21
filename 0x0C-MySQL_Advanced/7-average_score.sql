-- Create trigger to reset valid email
-- Is this the problem
DELIMETER $$
CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT)
BEGIN
    SET @scored = (
        SELECT AVG(score)
        FROM corrections WHERE corrections.user_id = user_id);
    UPDATE users SET average_score = @scored
    WHERE id = user_id;
END$$
DELIMETER ;
