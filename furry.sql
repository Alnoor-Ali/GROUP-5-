-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.25 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for furry
CREATE DATABASE IF NOT EXISTS `furry` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `furry`;

-- Dumping structure for table furry.appointment
CREATE TABLE IF NOT EXISTS `appointment` (
  `appointment_ID` varchar(50) NOT NULL,
  `appointment_date` date NOT NULL,
  `appointment_status` varchar(50) NOT NULL,
  `customer_name` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`appointment_ID`),
  KEY `FK_appointment_customer` (`customer_name`) USING BTREE,
  CONSTRAINT `FK_appointment_customer` FOREIGN KEY (`customer_name`) REFERENCES `customer` (`customer_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table furry.appointment: ~3 rows (approximately)
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
REPLACE INTO `appointment` (`appointment_ID`, `appointment_date`, `appointment_status`, `customer_name`) VALUES
	('A-001', '2000-02-01', 'Good', 'Carol'),
	('A-003', '2021-07-03', 'Ongoing', 'Joshua'),
	('A-004', '2021-01-01', 'Good', 'Carol');
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;

-- Dumping structure for table furry.customer
CREATE TABLE IF NOT EXISTS `customer` (
  `customer_ID` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `contact_number` int NOT NULL,
  `birthday` date NOT NULL,
  PRIMARY KEY (`customer_ID`),
  KEY `customer_name` (`customer_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table furry.customer: ~2 rows (approximately)
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
REPLACE INTO `customer` (`customer_ID`, `customer_name`, `contact_number`, `birthday`) VALUES
	('C-001', 'Joshua', 987, '2020-01-01'),
	('C-002', 'Carol', 1234, '2002-05-11');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;

-- Dumping structure for table furry.pet
CREATE TABLE IF NOT EXISTS `pet` (
  `pet_ID` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `pet_name` varchar(50) NOT NULL,
  `type_of_animal` varchar(50) NOT NULL,
  `breed` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `birthday` date NOT NULL,
  `customer_name` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`pet_ID`),
  KEY `customer_name` (`customer_name`),
  CONSTRAINT `FK_pet_customer` FOREIGN KEY (`customer_name`) REFERENCES `customer` (`customer_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table furry.pet: ~0 rows (approximately)
/*!40000 ALTER TABLE `pet` DISABLE KEYS */;
REPLACE INTO `pet` (`pet_ID`, `pet_name`, `type_of_animal`, `breed`, `gender`, `birthday`, `customer_name`) VALUES
	('P-001', 'Wololo', 'Dog', 'ASKLA', 'M', '2021-01-01', 'Carol'),
	('P-002', 'Oof', 'Cat', 'snoe mo', 'Male', '2021-08-09', 'Joshua'),
	('P-003', 'Koko', 'Bird', 'Parrot', 'RGB', '2021-08-09', 'Carol');
/*!40000 ALTER TABLE `pet` ENABLE KEYS */;

-- Dumping structure for table furry.user
CREATE TABLE IF NOT EXISTS `user` (
  `id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `username` varchar(50) NOT NULL,
  `role` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table furry.user: ~2 rows (approximately)
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
REPLACE INTO `user` (`id`, `username`, `role`, `password`) VALUES
	('U-001', 'marmar', 'admin', '1234'),
	('U-002', 'ross', 'staff', 'qwer');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
