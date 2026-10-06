-- MySQL dump 10.13  Distrib 8.4.11, for Linux (x86_64)
--
-- Host: localhost    Database: clase
-- ------------------------------------------------------
-- Server version	8.4.11-0ubuntu0.26.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ciclistas`
--

DROP TABLE IF EXISTS `ciclistas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ciclistas` (
  `nombre` varchar(100) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `fecha_de_nacimiento` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telefono` varchar(100) DEFAULT NULL,
  `Identificador` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Identificador`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciclistas`
--

LOCK TABLES `ciclistas` WRITE;
/*!40000 ALTER TABLE `ciclistas` DISABLE KEYS */;
INSERT INTO `ciclistas` VALUES ('Heverton','Marques Ferreira','1991-02-08','662353018','hevertonmf@gmail.com',1),('Mario','Moreira Silva','1875-25-08','662353018','Mario5558@gmail.com',2),('Tiago','Costa Almeida','1988-05-19','662353019','tiago.costa1@example.com',3),('Sofia','Pereira Silva','1994-11-03','662353020','sofia.pereira2@example.com',4),('Bruno','Rodrigues Santos','1986-07-27','662353021','bruno.rodrigues3@example.com',5),('Mariana','Carvalho Nunes','1992-01-15','662353022','mariana.carvalho4@example.com',6),('Ricardo','Oliveira Martins','1980-09-08','662353023','ricardo.oliveira5@example.com',7),('Beatriz','Sousa Lopes','1997-03-22','662353024','beatriz.sousa6@example.com',8),('André','Fernandes Gomes','1983-12-11','662353025','andre.fernandes7@example.com',9),('Catarina','Marques Teixeira','1995-06-30','662353026','catarina.marques8@example.com',10),('Nuno','Ribeiro Correia','1989-04-05','662353027','nuno.ribeiro9@example.com',11),('Inês','Machado Pinto','1990-08-17','662353028','ines.machado10@example.com',12),('Pedro','Cardoso Barbosa','1985-02-24','662353029','pedro.cardoso11@example.com',13),('Joana','Reis Coelho','1998-10-09','662353030','joana.reis12@example.com',14),('Miguel','Monteiro Vieira','1987-01-28','662353031','miguel.monteiro13@example.com',15),('Rita','Tavares Araújo','1993-05-13','662353032','rita.tavares14@example.com',16),('Hugo','Neves Moreira','1981-07-06','662353033','hugo.neves15@example.com',17),('Filipa','Antunes Cunha','1996-09-21','662353034','filipa.antunes16@example.com',18),('Diogo','Pires Freitas','1984-11-14','662353035','diogo.pires17@example.com',19),('Ana Luísa','Batista Andrade','1999-02-02','662353036','analuisa.batista18@example.com',20),('Rui','Guerreiro Miranda','1982-06-25','662353037','rui.guerreiro19@example.com',21),('Carla','Nogueira Pinheiro','1991-04-10','662353038','carla.nogueira20@example.com',22),('Luís','Azevedo Faria','1978-12-19','662353039','luis.azevedo21@example.com',23),('Vera','Lima Salgado','1994-08-08','662353040','vera.lima22@example.com',24),('Gonçalo','Rocha Simões','1986-03-16','662353041','goncalo.rocha23@example.com',25),('Helena','Alves Figueiredo','1990-10-27','662353042','helena.alves24@example.com',26),('Tomás','Santana Duarte','1988-01-04','662353043','tomas.santana25@example.com',27),('Cláudia','Faria Esteves','1997-07-19','662353044','claudia.faria26@example.com',28),('Fábio','Correia Pacheco','1983-05-31','662353045','fabio.correia27@example.com',29),('Sandra','Leal Campos','1992-09-14','662353046','sandra.leal28@example.com',30),('Vasco','Amaral Serra','1985-12-01','662353047','vasco.amaral29@example.com',31),('Margarida','Brito Cabral','1996-04-23','662353048','margarida.brito30@example.com',32),('Duarte','Cunha Bastos','1980-08-12','662353049','duarte.cunha31@example.com',33),('Alexandra','Freitas Nogueira','1993-11-06','662353050','alexandra.freitas32@example.com',34),('Martim','Andrade Coutinho','1987-02-20','662353051','martim.andrade33@example.com',35),('Daniela','Miranda Pimentel','1995-06-17','662353052','daniela.miranda34@example.com',36),('Eduardo','Pinheiro Valente','1979-10-03','662353053','eduardo.pinheiro35@example.com',37),('Sílvia','Faria Quintas','1998-01-29','662353054','silvia.faria36@example.com',38),('João','Salgado Portela','1984-07-08','662353055','joao.salgado37@example.com',39),('Teresa','Simões Abreu','1991-03-25','662353056','teresa.simoes38@example.com',40),('Manuel','Figueiredo Castanheira','1982-11-16','662353057','manuel.figueiredo39@example.com',41),('Cristiana','Duarte Xavier','1994-05-02','662353058','cristiana.duarte40@example.com',42),('Renato','Esteves Marinho','1986-09-27','662353059','renato.esteves41@example.com',43),('Ivone','Pacheco Braga','1989-12-09','662353060','ivone.pacheco42@example.com',44),('Sérgio','Campos Falcão','1981-04-14','662353061','sergio.campos43@example.com',45),('Bárbara','Serra Guedes','1997-08-28','662353062','barbara.serra44@example.com',46),('Leonardo','Cabral Correia','1985-10-19','662353063','leonardo.cabral45@example.com',47),('Ana Rita','Bastos Mendes','1993-02-06','662353064','anarita.bastos46@example.com',48),('Osvaldo','Nogueira Barroso','1978-06-21','662353065','osvaldo.nogueira47@example.com',49),('Marisa','Coutinho Peixoto','1996-11-11','662353066','marisa.coutinho48@example.com',50);
/*!40000 ALTER TABLE `ciclistas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `día que practicó`
--

DROP TABLE IF EXISTS `día que practicó`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `día que practicó` (
  `Identificador` int NOT NULL AUTO_INCREMENT,
  `ciclista_id` int DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`Identificador`),
  KEY `ciclista_id` (`ciclista_id`),
  CONSTRAINT `día que practicó_ibfk_1` FOREIGN KEY (`ciclista_id`) REFERENCES `ciclistas` (`Identificador`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `día que practicó`
--

LOCK TABLES `día que practicó` WRITE;
/*!40000 ALTER TABLE `día que practicó` DISABLE KEYS */;
INSERT INTO `día que practicó` VALUES (1,1,'2026-09-20'),(2,1,'2026-09-20'),(3,2,'2026-09-21'),(4,3,'2026-09-19'),(5,4,'2026-09-22'),(6,5,'2026-09-18'),(7,6,'2026-09-20'),(8,7,'2026-09-21'),(9,8,'2026-09-19'),(10,9,'2026-09-22'),(11,10,'2026-09-18'),(12,11,'2026-09-20'),(13,12,'2026-09-21'),(14,13,'2026-09-19'),(15,14,'2026-09-22'),(16,15,'2026-09-18'),(17,16,'2026-09-20'),(18,17,'2026-09-21'),(19,18,'2026-09-19'),(20,19,'2026-09-22'),(21,20,'2026-09-18'),(22,21,'2026-09-20'),(23,22,'2026-09-21'),(24,23,'2026-09-19'),(25,24,'2026-09-22'),(26,25,'2026-09-18'),(27,26,'2026-09-20'),(28,27,'2026-09-21'),(29,28,'2026-09-19'),(30,29,'2026-09-22'),(31,30,'2026-09-18'),(32,31,'2026-09-20'),(33,32,'2026-09-21'),(34,33,'2026-09-19'),(35,34,'2026-09-22'),(36,35,'2026-09-18'),(37,36,'2026-09-20'),(38,37,'2026-09-21'),(39,38,'2026-09-19'),(40,39,'2026-09-22'),(41,40,'2026-09-18'),(42,41,'2026-09-20'),(43,42,'2026-09-21'),(44,43,'2026-09-19'),(45,44,'2026-09-22'),(46,45,'2026-09-18'),(47,46,'2026-09-20'),(48,47,'2026-09-21'),(49,48,'2026-09-19'),(50,49,'2026-09-22'),(51,50,'2026-09-18');
/*!40000 ALTER TABLE `día que practicó` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meta de kilómetros`
--

DROP TABLE IF EXISTS `meta de kilómetros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `meta de kilómetros` (
  `Identificador` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `kilometros` decimal(10,2) DEFAULT NULL,
  `ciclista_id` int DEFAULT NULL,
  PRIMARY KEY (`Identificador`),
  KEY `ciclista_id` (`ciclista_id`),
  CONSTRAINT `meta de kilómetros_ibfk_1` FOREIGN KEY (`ciclista_id`) REFERENCES `ciclistas` (`Identificador`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meta de kilómetros`
--

LOCK TABLES `meta de kilómetros` WRITE;
/*!40000 ALTER TABLE `meta de kilómetros` DISABLE KEYS */;
INSERT INTO `meta de kilómetros` VALUES (1,'Heverton',50.00,NULL),(2,'Heverton',50.00,NULL),(3,'Mario',30.00,NULL),(4,'Tiago',45.50,NULL),(5,'Sofia',25.00,NULL),(6,'Bruno',60.00,NULL),(7,'Mariana',35.00,NULL),(8,'Ricardo',40.00,NULL),(9,'Beatriz',28.50,NULL),(10,'André',55.00,NULL),(11,'Catarina',32.00,NULL),(12,'Nuno',48.00,NULL),(13,'Inês',27.00,NULL),(14,'Pedro',52.00,NULL),(15,'Joana',30.50,NULL),(16,'Miguel',44.00,NULL),(17,'Rita',26.00,NULL),(18,'Hugo',58.00,NULL),(19,'Filipa',33.00,NULL),(20,'Diogo',47.00,NULL),(21,'Ana Luísa',29.00,NULL),(22,'Rui',51.00,NULL),(23,'Carla',31.50,NULL),(24,'Luís',46.00,NULL),(25,'Vera',24.00,NULL),(26,'Gonçalo',54.00,NULL),(27,'Helena',34.00,NULL),(28,'Tomás',43.00,NULL),(29,'Cláudia',28.00,NULL),(30,'Fábio',57.00,NULL),(31,'Sandra',32.50,NULL),(32,'Vasco',49.00,NULL),(33,'Margarida',26.50,NULL),(34,'Duarte',53.00,NULL),(35,'Alexandra',35.50,NULL),(36,'Martim',41.00,NULL),(37,'Daniela',27.50,NULL),(38,'Eduardo',56.00,NULL),(39,'Sílvia',33.50,NULL),(40,'João',45.00,NULL),(41,'Teresa',29.50,NULL),(42,'Manuel',50.50,NULL),(43,'Cristiana',31.00,NULL),(44,'Renato',42.00,NULL),(45,'Ivone',25.50,NULL),(46,'Sérgio',59.00,NULL),(47,'Bárbara',34.50,NULL),(48,'Leonardo',47.50,NULL),(49,'Ana Rita',28.50,NULL),(50,'Osvaldo',52.50,NULL),(51,'Marisa',30.00,NULL);
/*!40000 ALTER TABLE `meta de kilómetros` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-03 19:06:39
