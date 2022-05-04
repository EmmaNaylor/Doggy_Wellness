CREATE DATABASE  IF NOT EXISTS `dog_wellness_service` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dog_wellness_service`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dog_wellness_service
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `activity`
--

DROP TABLE IF EXISTS `activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activity` (
  `id` tinyint NOT NULL AUTO_INCREMENT,
  `activity_name` varchar(40) NOT NULL,
  `description` varchar(500) NOT NULL,
  `activity_type` enum('Group Class','1 to 1') NOT NULL,
  `supervision` enum('Stay and Play','Drop and Go') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activity`
--

LOCK TABLES `activity` WRITE;
/*!40000 ALTER TABLE `activity` DISABLE KEYS */;
INSERT INTO `activity` VALUES (1,'Yoga','A mindful class for you and your dog. Enjoy gentle stretches and holds to prepare your body for the day.','1 to 1','Stay and Play'),(2,'Canine Cardio','Get your dog\\\'s heart pumping with this high intensity work out.','1 to 1','Drop and Go'),(3,'Canine Circuit Training','From pat and squats to short sprints, this class will give you and your dog a full body workout.','Group Class','Stay and Play'),(4,'Doggy Zumba','Who says dogs can\\\'t dance? Some simple steps to fun music which will be sure to get you and your dog on your feet.','Group Class','Stay and Play'),(5,'Park Run','A classic 5k park run set up in an enclosed space for peace of mind. Take it as fast or slow as you like\\!','Group Class','Stay and Play'),(6,'Boxer-cise','A bouncy class suitable for larger breeds','Group Class','Stay and Play');
/*!40000 ALTER TABLE `activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `activity_recommendation`
--

DROP TABLE IF EXISTS `activity_recommendation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activity_recommendation` (
  `id` tinyint NOT NULL AUTO_INCREMENT,
  `dog_category` tinyint NOT NULL,
  `activity_recommendation` tinyint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dog_category` (`dog_category`),
  KEY `activity_recommendation` (`activity_recommendation`),
  CONSTRAINT `activity_recommendation_ibfk_1` FOREIGN KEY (`dog_category`) REFERENCES `dog_category` (`id`),
  CONSTRAINT `activity_recommendation_ibfk_2` FOREIGN KEY (`activity_recommendation`) REFERENCES `activity` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activity_recommendation`
--

LOCK TABLES `activity_recommendation` WRITE;
/*!40000 ALTER TABLE `activity_recommendation` DISABLE KEYS */;
INSERT INTO `activity_recommendation` VALUES (1,1,1),(2,2,1),(3,4,1),(4,5,1),(5,7,1),(6,8,1),(7,2,2),(8,3,2),(9,4,2),(10,5,2),(11,5,3),(12,6,3),(13,8,3),(14,9,3),(15,1,4),(16,2,4),(17,4,4),(18,5,4),(19,7,4),(20,8,4),(21,1,5),(22,2,5),(23,3,5),(24,4,5),(25,5,5),(26,6,5),(27,7,5),(28,8,5),(29,9,5);
/*!40000 ALTER TABLE `activity_recommendation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `id` smallint NOT NULL AUTO_INCREMENT,
  `customer_id` tinyint DEFAULT NULL,
  `dog_name` varchar(40) NOT NULL,
  `activity_id` tinyint NOT NULL,
  `event_id` tinyint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  KEY `dog_id` (`dog_name`),
  KEY `activity_id` (`activity_id`),
  KEY `event_id` (`event_id`),
  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`),
  CONSTRAINT `booking_ibfk_4` FOREIGN KEY (`event_id`) REFERENCES `event_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (1,1,'1',1,3),(2,1,'1',2,1),(3,1,'1',4,5),(4,1,'1',5,7),(5,2,'2',5,7),(6,2,'2',4,5),(7,2,'2',1,3),(8,3,'3',5,10),(9,3,'3',5,8),(10,1,'4',5,7),(29,84,'Chickpea',5,10),(30,86,'Troy',3,3),(31,89,'Jiggly',6,6),(32,92,'Pandabear',4,9);
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` tinyint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telephone_number` varchar(12) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'John','Smith','johnsmith@madeupemail.com','07821935481'),(2,'Angelina','Jolie','ang@madeupemail.com','07821935482'),(3,'David','Tennant','doctorwho@tardis.com','07821000487'),(4,'Sherlock','Holmes','sherlockandwatson@spy.com','07821115487'),(5,'Art','Garfunkel','soundofsilence@folk.com','07833335487'),(6,'Emma','Naylor','emmanaylz@gmail.com','07522505348'),(8,'Daniel','Guppy','Thebest@gmail.com','07522533444'),(9,'Fred','Hendrix','FredHed@gmail.com','07882100921'),(84,'Hilary','Blanc','Hilbil@gmail.com','07499888707'),(86,'Jessica','Messica','Jesmes@gmail.com','07882100875'),(87,'Terence','Berry','Terber@gmail.com','07555333271'),(88,'Arthur','Treeby','Artreeb@gmail.com','07555333616'),(89,'Hannah','Harker','Harker24@gmail.com','07888565432'),(90,'Emma','Naylor','emmanaylz@gmail.com','07522505348'),(91,'Quickcheck','Quickcheck','Quickcheck@gmail.com','07666555444'),(92,'Tory','Snorey','Torsnor@gmail.com','07522580707');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_booking`
--

DROP TABLE IF EXISTS `customer_booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_booking` (
  `id` tinyint NOT NULL AUTO_INCREMENT,
  `activity_name` varchar(100) NOT NULL,
  `event_date` date DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telephone_number` varchar(12) NOT NULL,
  `dog_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_booking`
--

LOCK TABLES `customer_booking` WRITE;
/*!40000 ALTER TABLE `customer_booking` DISABLE KEYS */;
INSERT INTO `customer_booking` VALUES (1,'Yoga','2022-04-21','10:30:00','Natalie','Beddow','dakfjhhjsaf@dkihSOIDY.com','29837892374','Doug');
/*!40000 ALTER TABLE `customer_booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dog`
--

DROP TABLE IF EXISTS `dog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dog` (
  `id` tinyint NOT NULL AUTO_INCREMENT,
  `dog_name` varchar(40) NOT NULL,
  `breed` varchar(40) DEFAULT NULL,
  `age` tinyint DEFAULT NULL,
  `size` enum('large','small','medium') DEFAULT NULL,
  `energy_level` enum('Couch Potato','Moderate','energetic') DEFAULT NULL,
  `temperament` tinyint DEFAULT NULL,
  `dog_owner` tinyint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `temperament` (`temperament`),
  KEY `dog_owner` (`dog_owner`),
  CONSTRAINT `dog_ibfk_2` FOREIGN KEY (`dog_owner`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dog`
--

LOCK TABLES `dog` WRITE;
/*!40000 ALTER TABLE `dog` DISABLE KEYS */;
INSERT INTO `dog` VALUES (1,'Marley','Labrador',2,'large','Moderate',2,1),(2,'Beethoven','St. Bernard',1,'large','Couch Potato',1,2),(3,'Lady','Cocker Spaniel',4,'small','energetic',9,3),(4,'Toto','Cairn Terrier',3,'small','Moderate',8,1),(5,'Copper','Coonhound',5,'medium','energetic',6,3),(6,'Lassie','Collie',5,'medium','energetic',6,2),(7,'Bruiser','Chihuahua',3,'small','Moderate',8,3),(8,'Frank','Pug',2,'small','Couch Potato',7,4),(9,'Santa\'s Little Helper','Greyhound',6,'medium','Moderate',5,5),(10,'Fly','Sheepdog',5,'medium','energetic',6,5),(17,'Chickpea',NULL,NULL,NULL,NULL,NULL,84),(18,'Troy',NULL,NULL,NULL,NULL,NULL,86),(19,'Jiggly',NULL,NULL,NULL,NULL,NULL,89),(20,'Pandabear',NULL,NULL,NULL,NULL,NULL,92);
/*!40000 ALTER TABLE `dog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dog_category`
--

DROP TABLE IF EXISTS `dog_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dog_category` (
  `id` tinyint NOT NULL AUTO_INCREMENT,
  `size` enum('large','medium','small') NOT NULL,
  `energy_level` enum('couch potato','moderate','energetic') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dog_category`
--

LOCK TABLES `dog_category` WRITE;
/*!40000 ALTER TABLE `dog_category` DISABLE KEYS */;
INSERT INTO `dog_category` VALUES (1,'large','couch potato'),(2,'large','moderate'),(3,'large','energetic'),(4,'medium','couch potato'),(5,'medium','moderate'),(6,'medium','energetic'),(7,'small','couch potato'),(8,'small','moderate'),(9,'small','energetic');
/*!40000 ALTER TABLE `dog_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_info`
--

DROP TABLE IF EXISTS `event_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_info` (
  `id` tinyint NOT NULL AUTO_INCREMENT,
  `activity_id` tinyint NOT NULL,
  `event_date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `duration` time NOT NULL,
  `cost` tinyint NOT NULL,
  `capacity` tinyint NOT NULL,
  `location` enum('online','The Dog House') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `event_info_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_info`
--

LOCK TABLES `event_info` WRITE;
/*!40000 ALTER TABLE `event_info` DISABLE KEYS */;
INSERT INTO `event_info` VALUES (1,2,'2022-05-27','10:30:00','11:30:00','01:00:00',5,10,'The Dog House'),(2,3,'2022-05-28','10:30:00','11:30:00','01:00:00',8,10,'The Dog House'),(3,1,'2022-06-29','07:30:00','08:00:00','00:30:00',6,10,'The Dog House'),(4,1,'2022-07-30','07:30:00','08:30:00','01:00:00',6,10,'The Dog House'),(5,4,'2022-07-01','18:30:00','19:30:00','01:00:00',0,5,'online'),(6,4,'2022-08-25','18:30:00','19:30:00','01:00:00',0,5,'online'),(7,5,'2022-09-23','09:00:00','09:30:00','00:30:00',0,5,'The Dog House'),(8,5,'2022-09-14','09:00:00','10:00:00','01:00:00',0,5,'The Dog House'),(9,2,'2022-10-15','18:30:00','19:30:00','01:00:00',5,4,'The Dog House'),(10,5,'2022-11-26','18:30:00','19:30:00','01:00:00',6,5,'The Dog House');
/*!40000 ALTER TABLE `event_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `full_address`
--

DROP TABLE IF EXISTS `full_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `full_address` (
  `id` smallint NOT NULL AUTO_INCREMENT,
  `first_line` varchar(100) NOT NULL,
  `second_line` varchar(100) DEFAULT NULL,
  `town` varchar(35) NOT NULL,
  `postcode` varchar(12) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `full_address`
--

LOCK TABLES `full_address` WRITE;
/*!40000 ALTER TABLE `full_address` DISABLE KEYS */;
INSERT INTO `full_address` VALUES (1,'1 Cherry Tree Avenue','Orchard Close','London','E17 9AP'),(2,'5 Coronation Street','Weatherfield','Greater Manchester','M12 4DS'),(3,'4 Privet Drive','Little Whinging','Surry','SA42 3LP'),(4,'221b Baker Street','Oxford Place','London','NW1 6XE'),(5,'Abbey Road Studios','3 Abbey Road','London','NW8 9AW');
/*!40000 ALTER TABLE `full_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` tinyint NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `user_password` varchar(100) DEFAULT NULL,
  `linked_customer` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `linked_customer` (`linked_customer`),
  CONSTRAINT `member_ibfk_1` FOREIGN KEY (`linked_customer`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (2,'spiderman@gmail.com','sha256$In9twZwcI9KaL8fD$a1689a4003e26e3c6db3737a6982f3156ee0c55b4b31a46777d41183194e5eec',NULL),(3,'Sally@gmail.com','sha256$qtpYHA8pAP98OMxa$44a5f36fb05b71c43b414bc5b573c0a92725ef38cf2b38a651f23dbb89c62aa6',NULL);
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `upcoming_event`
--

DROP TABLE IF EXISTS `upcoming_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `upcoming_event` (
  `id` tinyint NOT NULL AUTO_INCREMENT,
  `activity_id` tinyint NOT NULL,
  `event_info` tinyint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_id` (`activity_id`),
  KEY `event_info` (`event_info`),
  CONSTRAINT `upcoming_event_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`),
  CONSTRAINT `upcoming_event_ibfk_2` FOREIGN KEY (`event_info`) REFERENCES `event_info` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `upcoming_event`
--

LOCK TABLES `upcoming_event` WRITE;
/*!40000 ALTER TABLE `upcoming_event` DISABLE KEYS */;
/*!40000 ALTER TABLE `upcoming_event` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-29 15:34:25
