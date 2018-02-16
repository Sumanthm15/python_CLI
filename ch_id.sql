DELIMITER $$
 
USE school $$
 
CREATE PROCEDURE check_id(IN a_id int, OUT t int)
BEGIN

declare t1 int default 0;
declare t2 int default 0;
declare t3 int default 0;

select count(*) into t1 from management where m_id = a_id;
select count(*) into t2 from teacher where t_id = a_id;
select count(*) into t3 from student where s_id = a_id;

set t = t1 + t2 + t3;

 
END$$
 
DELIMITER ;