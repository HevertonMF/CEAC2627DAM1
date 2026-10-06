-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: biblioteca
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
-- Table structure for table `autores`
--

DROP TABLE IF EXISTS `autores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `autores` (
  `id_autor` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `nacionalidad` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_autor`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autores`
--

LOCK TABLES `autores` WRITE;
/*!40000 ALTER TABLE `autores` DISABLE KEYS */;
INSERT INTO `autores` VALUES (1,'Gabriel García Márquez','Colombiana'),(2,'George Orwell','Británica'),(3,'Miguel de Cervantes','Española'),(4,'Antoine de Saint-Exupéry','Francesa'),(5,'Yuval Noah Harari','Israelí'),(6,'Robert C. Martin','Estadounidense'),(7,'Andrew Hunt','Estadounidense'),(8,'J. K. Rowling','Británica'),(9,'J. R. R. Tolkien','Británica'),(10,'Ray Bradbury','Estadounidense'),(11,'James Clear','Estadounidense'),(12,'Robert Kiyosaki','Estadounidense'),(13,'Paulo Coelho','Brasileña'),(14,'José Saramago','Portuguesa'),(15,'Carlos Ruiz Zafón','Española'),(16,'Machado de Assis','Brasileña'),(17,'Fernando Pessoa','Portuguesa'),(18,'Clarice Lispector','Brasileña');
/*!40000 ALTER TABLE `autores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categorias` (
  `id_categoria` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id_categoria`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (9,'Autoayuda'),(12,'Biografía'),(2,'Ciencia ficción'),(3,'Clásico'),(6,'Ensayo'),(8,'Fantasía'),(10,'Finanzas'),(5,'Historia'),(4,'Infantil'),(1,'Novela'),(11,'Poesía'),(7,'Programación');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libros`
--

DROP TABLE IF EXISTS `libros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libros` (
  `id_libro` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(150) NOT NULL,
  `id_autor` int(11) NOT NULL,
  `id_categoria` int(11) NOT NULL,
  `paginas` int(11) DEFAULT NULL,
  `precio` decimal(6,2) DEFAULT NULL,
  `fecha_compra` date NOT NULL,
  `fecha_fin_lectura` date DEFAULT NULL,
  `valoracion` tinyint(4) DEFAULT NULL CHECK (`valoracion` between 1 and 5),
  PRIMARY KEY (`id_libro`),
  KEY `id_autor` (`id_autor`),
  KEY `id_categoria` (`id_categoria`),
  CONSTRAINT `libros_ibfk_1` FOREIGN KEY (`id_autor`) REFERENCES `autores` (`id_autor`),
  CONSTRAINT `libros_ibfk_2` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libros`
--

LOCK TABLES `libros` WRITE;
/*!40000 ALTER TABLE `libros` DISABLE KEYS */;
INSERT INTO `libros` VALUES (1,'Cien años de soledad',1,1,471,21.90,'2024-01-15','2024-03-02',5),(2,'El amor en los tiempos del cólera',1,1,464,19.50,'2024-05-10','2024-07-01',4),(3,'1984',2,2,352,12.95,'2024-02-03','2024-02-25',5),(4,'Rebelión en la granja',2,1,144,9.95,'2024-02-03','2024-02-10',4),(5,'Don Quijote de la Mancha',3,3,1376,25.00,'2024-03-20',NULL,NULL),(6,'El principito',4,4,96,8.50,'2024-04-01','2024-04-03',5),(7,'Sapiens: de animales a dioses',5,5,496,22.90,'2024-06-12','2024-08-20',5),(8,'Homo Deus: breve historia del mañana',5,6,496,22.90,'2024-09-05','2024-11-15',4),(9,'Código limpio',6,7,464,39.90,'2025-01-10','2025-03-30',5),(10,'El programador pragmático',7,7,352,42.00,'2025-02-14',NULL,NULL),(11,'Harry Potter y la piedra filosofal',8,8,256,15.95,'2024-07-07','2024-07-20',4),(12,'El Señor de los Anillos: La Comunidad del Anillo',9,8,576,23.95,'2024-10-01','2024-12-10',5),(13,'El hobbit',9,8,320,14.95,'2024-08-15','2024-09-01',4),(14,'Fahrenheit 451',10,2,192,10.95,'2025-03-05','2025-03-18',4),(15,'Hábitos atómicos',11,9,336,19.90,'2025-01-02','2025-01-28',4),(16,'Padre rico, padre pobre',12,10,272,16.90,'2025-04-11','2025-05-02',3),(17,'El alquimista',13,1,192,12.90,'2025-05-20','2025-05-30',3),(18,'Ensayo sobre la ceguera',14,1,432,20.90,'2025-07-01','2025-08-14',5),(19,'La sombra del viento',15,1,576,21.90,'2025-09-10',NULL,NULL),(20,'Dom Casmurro',16,3,256,11.50,'2026-01-08','2026-02-20',4);
/*!40000 ALTER TABLE `libros` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-06 10:53:28
