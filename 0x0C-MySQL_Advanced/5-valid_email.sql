-- Create trigger to reset valid email
-- Is this the problem
DELIMETER |
CREATE TRIGGER email_reset BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
    SET NEW.valid_email = 0;
    END IF;
END;
|
