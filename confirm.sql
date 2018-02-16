DELIMITER $$
 
USE school $$
 
CREATE PROCEDURE confirm(IN f_id int, IN pwd varchar(45), out a varchar(1))
BEGIN

declare t1 int default 0;
declare t2 int default 0;
declare t3 int default 0;

select count(*) into t1 from management where m_id = f_id AND m_password = pwd;
select count(*) into t2 from teacher where t_id = f_id AND t_password = pwd;
select count(*) into t3 from student where s_id = f_id AND s_password = pwd;

if t1 > 0 then set a ='m';
elseif t2 > 0 then set a = 't';
elseif t3 > 0 then set a = 's';
end if;
END$$
 
DELIMITER ;