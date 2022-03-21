-- IN this year of 2022 EVERYTHINGS a TRIGGER
CREATE TRIGGER make_it_less AFTER INSERT ON orders
FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
