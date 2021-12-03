-- pdfdatos.datos definition

CREATE TABLE `datos` (
  `contraseña` varchar(100),
  `dip` varchar(20),
  `so` varchar(100),
  `version` varchar(100),
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
);
