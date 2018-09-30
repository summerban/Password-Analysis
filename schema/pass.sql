DROP DATABASE IF EXISTS `passanlysis`;

CREATE DATABASE `passanlysis` DEFAULT CHARACTER SET utf8 collate utf8_general_ci;

use `passanlysis`;

CREATE TABLE `info` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(64) NOT NULL,
  `password` VARCHAR(64) NOT NULL,
  `email` VARCHAR(64) NULL,
  PRIMARY KEY (`id`)
);

CREATE USER IF NOT EXISTS 'passanlysis'@'localhost' IDENTIFIED BY 'random_password';
GRANT all privileges ON passanlysis.* TO 'passanlysis'@'localhost';

CREATE USER IF NOT EXISTS 'backup'@'localhost' IDENTIFIED BY 'another_random_password';
GRANT SELECT ON passanlysis.* TO 'backup'@'localhost';
