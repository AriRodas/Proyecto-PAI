-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: quality_transport
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `reservacion`
--

DROP TABLE IF EXISTS `reservacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservacion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) NOT NULL,
  `fecha` datetime NOT NULL,
  `servicio` varchar(100) NOT NULL,
  `pasajeros` varchar(45) NOT NULL,
  `partida` varchar(45) NOT NULL,
  `destino` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservacion`
--

LOCK TABLES `reservacion` WRITE;
/*!40000 ALTER TABLE `reservacion` DISABLE KEYS */;
INSERT INTO `reservacion` VALUES (2,'melitoledo','2021-07-23 00:00:00','Traslado hasta el aeropuerto','1991','aeropuerto monseñor Romero','Hotel sheraton presidente'),(3,'arirodas','2021-07-30 00:00:00','Traslados dentro y fuera de El Salvador','1984','Residencial finca de asturias','Aeropuerto'),(4,'melitoledo','2021-07-28 00:00:00','Transporte turístico','1986','Santa Ana','Ataco'),(5,'melitoledo','2021-07-21 00:00:00','Instituciones educativas','1993','esen','multi');
/*!40000 ALTER TABLE `reservacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicios`
--

DROP TABLE IF EXISTS `servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(250) NOT NULL,
  `descripcion` varchar(450) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicios`
--

LOCK TABLES `servicios` WRITE;
/*!40000 ALTER TABLE `servicios` DISABLE KEYS */;
INSERT INTO `servicios` VALUES (1,'Traslados dentro y fuera de El Salvador','Como parte del desarrollo de tu actividad comercial, ya sea para reuniones de negocios, visitas técnicas, envío y entrega de documentos importantes, entre otros.'),(2,'Traslado hasta el aeropuerto','Sabemos la importancia de las conexiones, y lo que significa para ti viajar seguro y llegar a tiempo. Desde tu hogar u oficina, desde o hacia el aeropuerto, nos esmeramos en ser confiables y hacer que tu viaje sea confortable.'),(3,'Transporte turístico','Disfrutar, tener vivencias únicas y poseer memorias increíbles de nuestro bello país es incomparable. ¡tienes que vivirlo! El Salvador posee una variedad de atractivos turísticos. Conocemos sus ciudades, sus pueblos vivos, su gente y nos encanta acompañarte'),(5,'Transporte de personal de trabajo','Movilizamos a su personal antes o después de su jornada laboral. Lo hacemos con grato placer y le ofrecemos un trato respetuoso y preferencial para cada uno de sus colaboradores. En unidades para 10, 15, 28 o más pasajeros'),(6,'Transporte para eventos y convenciones','Nos volvemos parte de tu marca y nos adaptamos para hacer de tu evento un éxito. Con capacidad y experiencia en logística para movilizar grupos de más de 100 personas'),(7,'Instituciones educativas','Volverte parte de algo siempre tiene un significado especial. Trabajamos con instituciones educativas para llevar a niños, jóvenes, padres de familia y docentes a diferentes actividades de esparcimiento o curriculares. Poseemos excelentes relaciones con escuelas públicas, colegios privados, universidades y centros de enseñanza'),(8,'Instituciones educativas','Volverte parte de algo siempre tiene un significado especial. Trabajamos con instituciones educativas para llevar a niños, jóvenes, padres de familia y docentes a diferentes actividades de esparcimiento o curriculares. Poseemos excelentes relaciones con escuelas públicas, colegios privados, universidades y centros de enseñanza');
/*!40000 ALTER TABLE `servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `role` varchar(45) NOT NULL,
  `password` varchar(75) NOT NULL,
  `salt` varchar(605) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'quality_transport','ventas@qtransportsv.com','admin','$2b$14$wXZVb64GL/ZfvT4ZAiax4uI6cVF3UV3nAf3AgLw97skdZG.gZ6cS2','$2b$14$wXZVb64GL/ZfvT4ZAiax4u'),(2,'melitoledo','melitoledo5@gmail.com','client','$2b$14$qdRtbiXUUjOLJJPGOOZsl..Z0qJJdriLL8pDiV6gnmQm.FYC7eaDy','$2b$14$qdRtbiXUUjOLJJPGOOZsl.'),(3,'gabri','gabrielaargueta2101@gmail.com','client','$2b$14$8Z5ViavIi0Z5I8GT9luKH.E6lfEiUDuMJeTG5SKdtJWhbjlD47JzW','$2b$14$8Z5ViavIi0Z5I8GT9luKH.'),(4,'arirodas','arirodas02@gmail.com','client','$2b$14$00Hg6l/dv9gQyyFUvHLCte705QVJwIejpumMKNaINFN/NQQgM/PZe','$2b$14$00Hg6l/dv9gQyyFUvHLCte');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-16 14:10:11
