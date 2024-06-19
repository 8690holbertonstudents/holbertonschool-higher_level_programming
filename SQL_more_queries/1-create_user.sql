-- script that creates user user_0d_1 on MySql-Server
-- user_0d_1 should have all privileges
-- user_0d_1 password should be set to user_0d_1_pwd
-- if user_0d_1 exists, script should not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';