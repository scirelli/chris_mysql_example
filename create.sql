CREATE DATABASE `chris_example` /*!40100 DEFAULT CHARACTER SET latin1 */;

CREATE TABLE `test_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `last_name` varchar(45) DEFAULT NULL,
  `some_other_data` varchar(45) DEFAULT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
