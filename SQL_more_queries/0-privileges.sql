-- script that lists all privileges
CREATE USER 'user_0d_1'@'localhost';
CREATE USER 'user_0d_2'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost, user_0d_2@localhost
