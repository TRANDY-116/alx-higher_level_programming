-- Creates myswl user user_0s_1
--	*Havinh all priviledges on the mysql server
--	*password should be user_0d_1_pwd
--	*if the user exist the script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
