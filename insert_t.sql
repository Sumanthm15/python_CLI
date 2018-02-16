DELIMITER $$
 
USE school $$
 
CREATE PROCEDURE insert_teacher(IN f_id int, f_name varchar(45), pwd varchar(45), sub varchar(45))
BEGIN

 INSERT INTO teacher values (f_id, f_name, pwd, sub);
 
END$$
 
DELIMITER ;