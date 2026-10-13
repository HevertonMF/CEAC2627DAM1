-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: ciudades
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `ciudades`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `ciudades` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `ciudades`;

--
-- Table structure for table `ciudades`
--

DROP TABLE IF EXISTS `ciudades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ciudades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ciudades` varchar(100) DEFAULT NULL,
  `país` varchar(100) DEFAULT NULL,
  `continente` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciudades`
--

LOCK TABLES `ciudades` WRITE;
/*!40000 ALTER TABLE `ciudades` DISABLE KEYS */;
INSERT INTO `ciudades` VALUES (2,'Sete Lagoas','Brasil','América del Sur'),(3,'São Paulo','Brasil','América del Sur'),(4,'Río de Janeiro','Brasil','América del Sur'),(5,'Belo Horizonte','Brasil','América del Sur'),(6,'Buenos Aires','Argentina','América del Sur'),(7,'Córdoba','Argentina','América del Sur'),(8,'Santiago','Chile','América del Sur'),(9,'Lima','Perú','América del Sur'),(10,'Bogotá','Colombia','América del Sur'),(11,'Medellín','Colombia','América del Sur'),(12,'Montevideo','Uruguay','América del Sur'),(13,'Quito','Ecuador','América del Sur'),(14,'Caracas','Venezuela','América del Sur'),(15,'Ciudad de México','México','América del Norte'),(16,'Guadalajara','México','América del Norte'),(17,'Nueva York','Estados Unidos','América del Norte'),(18,'Los Ángeles','Estados Unidos','América del Norte'),(19,'Chicago','Estados Unidos','América del Norte'),(20,'Toronto','Canadá','América del Norte'),(21,'Montreal','Canadá','América del Norte'),(22,'La Habana','Cuba','América Central'),(23,'San José','Costa Rica','América Central'),(24,'Ciudad de Panamá','Panamá','América Central'),(25,'Madrid','España','Europa'),(26,'Barcelona','España','Europa'),(27,'Valencia','España','Europa'),(28,'Sevilla','España','Europa'),(29,'Lisboa','Portugal','Europa'),(30,'Oporto','Portugal','Europa'),(31,'París','Francia','Europa'),(32,'Roma','Italia','Europa'),(33,'Milán','Italia','Europa'),(34,'Berlín','Alemania','Europa'),(35,'Londres','Reino Unido','Europa'),(36,'Ámsterdam','Países Bajos','Europa'),(37,'Atenas','Grecia','Europa'),(38,'Tokio','Japón','Asia'),(39,'Pekín','China','Asia'),(40,'Shanghái','China','Asia'),(41,'Seúl','Corea del Sur','Asia'),(42,'Bombay','India','Asia'),(43,'Bangkok','Tailandia','Asia'),(44,'Estambul','Turquía','Asia'),(45,'El Cairo','Egipto','África'),(46,'Lagos','Nigeria','África'),(47,'Nairobi','Kenia','África'),(48,'Ciudad del Cabo','Sudáfrica','África'),(49,'Casablanca','Marruecos','África'),(50,'Sídney','Australia','Oceanía'),(51,'Auckland','Nueva Zelanda','Oceanía');
/*!40000 ALTER TABLE `ciudades` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-11 14:09:31
