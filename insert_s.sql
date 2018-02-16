DELIMITER $$
 
USE school $$
 
CREATE PROCEDURE insert_student(IN f_id int, f_name varchar(45), pwd varchar(45), dep varchar(45))
BEGIN

 INSERT INTO student values (f_id, f_name, pwd, dep);
 
END$$
 
DELIMITER ;