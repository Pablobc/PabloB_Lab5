-- pdfdatos.datos definition

CREATE TABLE `datos` (
  `contraseña` varchar(100) NOT NULL,
  `dip` varchar(20) NOT NULL,
  `so` varchar(100) NOT NULL,
  `version` varchar(100) NOT NULL,
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
);
