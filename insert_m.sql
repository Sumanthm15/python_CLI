DELIMITER $$
 
USE school $$
 
CREATE PROCEDURE insert_management(IN f_id int, f_name varchar(45), pwd varchar(45))
BEGIN

 INSERT INTO management values (f_id, f_name, pwd);
 
END$$
 
DELIMITER ;