CREATE DATABASE urban_oasis;
CREATE USER 'urban_oasis_user'@'localhost' IDENTIFIED BY 'Doneddie@123';
GRANT ALL PRIVILEGES ON urban_oasis.* TO 'urban_oasis_user'@'localhost';

USE urban_oasis;
SHOW tables;

SELECT * FROM django_session;


