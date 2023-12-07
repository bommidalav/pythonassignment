-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.28-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for sales_system
CREATE DATABASE IF NOT EXISTS `sales_system` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `sales_system`;

-- Dumping structure for table sales_system.customer
CREATE TABLE IF NOT EXISTS `customer` (
  `CustomerID` varchar(50) DEFAULT NULL,
  `CustomerName` varchar(50) DEFAULT NULL,
  `AccountInfo` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table sales_system.customer: ~3 rows (approximately)
REPLACE INTO `customer` (`CustomerID`, `CustomerName`, `AccountInfo`) VALUES
	('1', 'Archie', 'q†Ëšj\\\n÷©§ùmíƒÏ'),
	('2', 'Buddy', 'Ë&>£ºNßø4mïPl');

-- Dumping structure for table sales_system.products
CREATE TABLE IF NOT EXISTS `products` (
  `ProductName` varchar(50) DEFAULT NULL,
  `ProductID` varchar(50) DEFAULT NULL,
  `Cost` float DEFAULT NULL,
  `InStock` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table sales_system.products: ~3 rows (approximately)
REPLACE INTO `products` (`ProductName`, `ProductID`, `Cost`, `InStock`) VALUES
	('argle', 'a1', 5, 100),
	('bargle', 'b1', 2.5, 200),
	('cargle', 'c1', 1.25, 200);

-- Dumping structure for table sales_system.sales
CREATE TABLE IF NOT EXISTS `sales` (
  `customer_id` varchar(50) DEFAULT NULL,
  `product_id` varchar(50) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_cost` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table sales_system.sales: ~2 rows (approximately)
REPLACE INTO `sales` (`customer_id`, `product_id`, `quantity`, `total_cost`) VALUES
	('1', 'a1', 5, 25);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
