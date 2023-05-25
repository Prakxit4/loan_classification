-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: projects
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account` (
  `account_id` varchar(10) NOT NULL,
  `user_id` int DEFAULT NULL,
  `balance` float DEFAULT NULL,
  PRIMARY KEY (`account_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `account_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES ('1445220136',2,45000);
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan`
--

DROP TABLE IF EXISTS `loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loan` (
  `loan_id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) DEFAULT NULL,
  `amount_paid` float DEFAULT '0',
  `loan_amount` float DEFAULT NULL,
  `loan_term` float DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `account_no` varchar(14) DEFAULT NULL,
  PRIMARY KEY (`loan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan`
--

LOCK TABLES `loan` WRITE;
/*!40000 ALTER TABLE `loan` DISABLE KEYS */;
INSERT INTO `loan` VALUES (1,'1',0,250000,7,'2027-03-10 00:00:00',NULL),(2,'1',0,250000,7,'2023-03-10 00:00:00',NULL),(3,'1',0,250000,7,'2023-03-10 00:00:00',NULL),(4,'1',0,250000,7,'2023-03-10 00:00:00',NULL),(5,'1',0,250000,7,'2023-03-10 00:00:00',NULL),(6,'1',0,250000,7,'2023-03-10 00:00:00',NULL),(7,'1',0,250000,7,'2023-03-10 00:00:00',NULL),(8,'1',0,250000,7,'2023-03-10 00:00:00',NULL),(9,'2',0,250000,7,'2023-03-11 00:00:00',NULL),(10,'2',0,250000,7,'2023-03-11 00:00:00',NULL),(11,NULL,0,250000,23.34,'2023-04-11 00:00:00','1445220136'),(12,NULL,0,250000,7,'2023-04-11 00:00:00','1445220137'),(13,NULL,0,250000,23.34,'2023-04-11 00:00:00','1445220135'),(14,NULL,0,250000,7,'2023-04-20 00:00:00','1445220139'),(15,NULL,0,2500000,2,'2023-04-20 00:00:00','1445220130'),(16,NULL,0,2500000,2,'2023-04-20 00:00:00','1445220131'),(17,NULL,0,2500000,1,'2023-04-20 00:00:00','1445220129'),(18,NULL,0,2500,1,'2023-04-20 00:00:00','1445220128'),(19,NULL,0,250,1,'2023-04-20 00:00:00','1445220127'),(20,NULL,0,2500000,850,'2023-04-20 00:00:00','1445220126'),(21,NULL,0,2500000,455,'2023-04-22 00:00:00','1445220125'),(22,NULL,0,250000,7,'2023-05-20 00:00:00','1445220160'),(23,NULL,0,250000,7,'2023-05-20 00:00:00','1445220149'),(24,NULL,0,250000,7,'2023-05-20 00:00:00','1445220169');
/*!40000 ALTER TABLE `loan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `role` varchar(255) DEFAULT 'user',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Kabita Panday','kabita@gmail.com','kabita@123','admin'),(2,'john doe','john','john@gmail.com','user'),(3,'Prakshit Poudel','123','prakshit@gmail.com','user'),(4,'Simran Aryal','simran@123','simran@gmail.com','user');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-20 12:18:49
