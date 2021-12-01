CREATE USER IF NOT EXISTS 'pdfhacker'@'localhost' IDENTIFIED BY 'ITKBWiCF';

CREATE DATABASE pdfdatos;

GRANT ALL PRIVILEGES ON pdfdatos.* TO 'pdfhacker'@'localhost';

FLUSH PRIVILEGES;