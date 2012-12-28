-- MySQL dump 10.13  Distrib 5.5.28, for osx10.7 (i386)
--
-- Host: localhost    Database: jminee
-- ------------------------------------------------------
-- Server version	5.5.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL,
  `content` varchar(5000) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `creator_id` int(11) NOT NULL,
  `deleted` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`uid`),
  KEY `subject_id` (`subject_id`),
  KEY `creator_id` (`creator_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`uid`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`creator_id`) REFERENCES `tg_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (2,'2012-12-26 23:53:13','This hw due in 12/12/12',10,5,0),(3,'2012-12-26 23:53:13','This hw due in 12/30/12',11,5,0),(4,'2012-12-27 00:19:44','On 12/30/12',12,5,0),(5,'2012-12-27 01:02:18','Due on 01/12',13,5,0),(6,'2012-12-27 01:02:18','Due on 02/13',14,5,0),(7,'2012-12-27 01:02:18','Due on 02/24',15,5,0),(8,'2012-12-27 01:02:18','Due on 12/04',16,5,0),(9,'2012-12-27 01:02:18','Please see the attachement',17,5,0),(10,'2012-12-28 11:42:09','Is this a 2 hours exam?',10,5,0),(11,'2012-12-28 11:50:11','Yes it is.',10,5,0),(12,'2012-12-28 11:51:42','That is too long, TA!',10,5,0),(13,'2012-12-28 11:52:24','It has been like this forever :)',10,5,0),(14,'2012-12-28 11:55:30','thanks!',10,5,0),(16,'2012-12-28 11:55:30','Another question, when is the due data of the final project?',10,5,0),(17,'2012-12-28 11:55:30','Have you seen my last question?',10,5,0),(18,'2012-12-28 11:55:30','It will be due a week after final.',10,5,0),(19,'2012-12-28 12:37:33','It will be due a week after final.',10,5,0),(20,'2012-12-28 12:47:47','You forgot the attachment.',13,5,0),(21,'2012-12-28 12:53:32','Oops, sorry!',13,5,0),(22,'2012-12-28 14:18:42','How can I submit my HW?',13,5,0),(23,'2012-12-28 14:20:13','You can attach it here.',13,5,0),(24,'2012-12-28 14:20:27','Did you get mine?',13,5,0),(31,'2012-12-28 15:33:16','Please register for the trip.',27,5,0),(32,'2012-12-28 15:34:02','Bach, John, Vinay',28,5,0),(33,'2012-12-28 15:34:14','Hey, I would like to go',27,5,0),(34,'2012-12-28 15:34:50','Me too!',27,5,0);
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment_subject`
--

DROP TABLE IF EXISTS `comment_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment_subject` (
  `comment_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`comment_id`,`subject_id`),
  KEY `subject_id` (`subject_id`),
  CONSTRAINT `comment_subject_ibfk_1` FOREIGN KEY (`comment_id`) REFERENCES `comment` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `comment_subject_ibfk_2` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment_subject`
--

LOCK TABLES `comment_subject` WRITE;
/*!40000 ALTER TABLE `comment_subject` DISABLE KEYS */;
INSERT INTO `comment_subject` VALUES (2,10,0),(3,11,0),(4,12,0),(5,13,0),(6,14,0),(7,15,0),(8,16,0),(9,17,0);
/*!40000 ALTER TABLE `comment_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_subject`
--

DROP TABLE IF EXISTS `member_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member_subject` (
  `member_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `last_read` int(11) NOT NULL,
  `muted` tinyint(1) NOT NULL,
  PRIMARY KEY (`member_id`,`subject_id`),
  KEY `subject_id` (`subject_id`),
  KEY `last_read` (`last_read`),
  CONSTRAINT `member_subject_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `tg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `member_subject_ibfk_2` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `member_subject_ibfk_3` FOREIGN KEY (`last_read`) REFERENCES `comment` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_subject`
--

LOCK TABLES `member_subject` WRITE;
/*!40000 ALTER TABLE `member_subject` DISABLE KEYS */;
INSERT INTO `member_subject` VALUES (5,10,2,0),(5,11,3,0),(5,12,4,0),(5,13,5,0),(5,14,6,0),(5,15,7,0),(5,16,8,0),(5,17,9,0),(5,27,31,0),(5,28,32,0);
/*!40000 ALTER TABLE `member_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_topic`
--

DROP TABLE IF EXISTS `member_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member_topic` (
  `member_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `role` varchar(2) NOT NULL,
  `local_title` varchar(255) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `unsubscribed` tinyint(1) NOT NULL,
  PRIMARY KEY (`member_id`,`topic_id`),
  KEY `topic_id` (`topic_id`),
  CONSTRAINT `member_topic_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `tg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `member_topic_ibfk_2` FOREIGN KEY (`topic_id`) REFERENCES `topic` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_topic`
--

LOCK TABLES `member_topic` WRITE;
/*!40000 ALTER TABLE `member_topic` DISABLE KEYS */;
INSERT INTO `member_topic` VALUES (5,16,'c','CS 273 / OS',0,0),(5,17,'c','Hadoop Performance',0,0),(5,18,'c','CS 431 / Real-time Systems',0,0),(5,19,'c','Niagra Fall camping',0,0),(5,20,'c','Dine out Friday with the Gang',0,0),(5,21,'c','Basketball Tournament',0,0),(5,22,'c','\'Web Monkey\'',0,0);
/*!40000 ALTER TABLE `member_topic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migrate_version`
--

DROP TABLE IF EXISTS `migrate_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `migrate_version` (
  `repository_id` varchar(250) NOT NULL,
  `repository_path` text,
  `version` int(11) DEFAULT NULL,
  PRIMARY KEY (`repository_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migrate_version`
--

LOCK TABLES `migrate_version` WRITE;
/*!40000 ALTER TABLE `migrate_version` DISABLE KEYS */;
INSERT INTO `migrate_version` VALUES ('migration','migration',0);
/*!40000 ALTER TABLE `migrate_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration_registration`
--

DROP TABLE IF EXISTS `registration_registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registration_registration` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime DEFAULT NULL,
  `user_name` varchar(255) NOT NULL,
  `email_address` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  `activated` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `registration_registration_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tg_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration_registration`
--

LOCK TABLES `registration_registration` WRITE;
/*!40000 ALTER TABLE `registration_registration` DISABLE KEYS */;
INSERT INTO `registration_registration` VALUES (1,'2012-06-26 04:03:55','bachbui@gmail.com','bachbui@gmail.com','******','468bfdef928477ff6138a795f3bb15f4ac0d40c0ea4a153da48efe2b5c40a568','2012-06-26 04:04:37',7),(2,'2012-06-26 17:24:59','robert.m.pieta@gmail.com','robert.m.pieta@gmail.com','******','7a8f1e47d2fee83ca06d3248d610383eee4c1bacf7128611fd40f78a3c5bce13','2012-06-26 17:25:10',8),(3,'2012-06-26 23:53:56','bobobagle@gmail.com','bobobagle@gmail.com','******','d0d3744b178c1547d5b3d2f09416875637e2ff94f8b2f5429835ce3785821909','2012-06-26 23:54:06',9);
/*!40000 ALTER TABLE `registration_registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration_resetpassword`
--

DROP TABLE IF EXISTS `registration_resetpassword`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registration_resetpassword` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime DEFAULT NULL,
  `email_address` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  `reset` datetime DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration_resetpassword`
--

LOCK TABLES `registration_resetpassword` WRITE;
/*!40000 ALTER TABLE `registration_resetpassword` DISABLE KEYS */;
/*!40000 ALTER TABLE `registration_resetpassword` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subject` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL,
  `title` varchar(255) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `creator_id` int(11) NOT NULL,
  PRIMARY KEY (`uid`),
  KEY `topic_id` (`topic_id`),
  KEY `creator_id` (`creator_id`),
  CONSTRAINT `subject_ibfk_1` FOREIGN KEY (`topic_id`) REFERENCES `topic` (`uid`),
  CONSTRAINT `subject_ibfk_2` FOREIGN KEY (`creator_id`) REFERENCES `tg_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES (10,'2012-12-26 23:53:13','Homework 1',16,5),(11,'2012-12-26 23:53:13','Homework 3',16,5),(12,'2012-12-27 00:19:44','Midterm Exam',16,5),(13,'2012-12-27 01:02:18','Homework 4',16,5),(14,'2012-12-27 01:02:18','Homework 5',16,5),(15,'2012-12-27 01:02:18','Homework 6',16,5),(16,'2012-12-27 01:02:18','Final exam',16,5),(17,'2012-12-27 01:02:18','First class material',18,5),(27,'2012-12-28 15:33:16','Registration',19,5),(28,'2012-12-28 15:34:02','Organizer',19,5);
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tg_group`
--

DROP TABLE IF EXISTS `tg_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tg_group` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(16) NOT NULL,
  `display_name` varchar(255) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  PRIMARY KEY (`group_id`),
  UNIQUE KEY `group_name` (`group_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tg_group`
--

LOCK TABLES `tg_group` WRITE;
/*!40000 ALTER TABLE `tg_group` DISABLE KEYS */;
INSERT INTO `tg_group` VALUES (1,'managers','Managers Group','2012-05-29 03:53:08');
/*!40000 ALTER TABLE `tg_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tg_group_permission`
--

DROP TABLE IF EXISTS `tg_group_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tg_group_permission` (
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`group_id`,`permission_id`),
  KEY `permission_id` (`permission_id`),
  CONSTRAINT `tg_group_permission_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `tg_group` (`group_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tg_group_permission_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `tg_permission` (`permission_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tg_group_permission`
--

LOCK TABLES `tg_group_permission` WRITE;
/*!40000 ALTER TABLE `tg_group_permission` DISABLE KEYS */;
INSERT INTO `tg_group_permission` VALUES (1,1);
/*!40000 ALTER TABLE `tg_group_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tg_permission`
--

DROP TABLE IF EXISTS `tg_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tg_permission` (
  `permission_id` int(11) NOT NULL AUTO_INCREMENT,
  `permission_name` varchar(63) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`permission_id`),
  UNIQUE KEY `permission_name` (`permission_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tg_permission`
--

LOCK TABLES `tg_permission` WRITE;
/*!40000 ALTER TABLE `tg_permission` DISABLE KEYS */;
INSERT INTO `tg_permission` VALUES (1,'manage','This permission give an administrative right to the bearer');
/*!40000 ALTER TABLE `tg_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tg_user`
--

DROP TABLE IF EXISTS `tg_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tg_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) NOT NULL,
  `email_address` varchar(255) NOT NULL,
  `display_name` varchar(255) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_name` (`user_name`),
  UNIQUE KEY `email_address` (`email_address`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tg_user`
--

LOCK TABLES `tg_user` WRITE;
/*!40000 ALTER TABLE `tg_user` DISABLE KEYS */;
INSERT INTO `tg_user` VALUES (1,'manager','manager@somedomain.com','Example manager','0607a1ec213e4869be95d248601eeb06b3cb54264080677438708eab151764b6be43ef7839696efef96cc7f736e3ed798a1d4e2cf47399d106c1814660cd4750','2012-05-29 03:53:08'),(2,'editor','editor@somedomain.com','Example editor','852b7efdf417359e69becfc0e03f485d55b777b1888c560720586627c56ca54bb4afd881f2a773d5564d07f6bd78faa70596aac95bb5418af0a81e01c9a66510','2012-05-29 03:53:08'),(3,'vhiremath4','vhiremath4@gmail.com','vhiremath4','ced81f4edf1e556ba0b287400c273958f76d671b65032993f8962a80dafdaec24b47b2d5b710ae1fcd2b2fd78edcc520843a01cd86b61b1af371e5eb27a28808','2012-05-30 08:16:31'),(5,'testuser','bui.duybach@gmail.com','testuser','c8bad6205a500379111cf9d99ca8bc8a1cfbf8edb341b54b9ab051d9f87ba055a802461c4a9f02247df4966d43f6f3feea75ab869fc05c9e55b8dfd91bbc58c1','2012-06-20 02:04:19'),(7,'bachbui@gmail.com','bachbui@gmail.com','bachbui@gmail.com','4c565b6c2c3e7e1334a2b55f764f01a4c25d827be2d41d7f10653bf97a4ff80c36db001b88aa8b4fb39974f059a0095f6e6ce6f2e49b312064c78db26846dd06','2012-06-26 04:04:37'),(8,'robert.m.pieta@gmail.com','robert.m.pieta@gmail.com','robert.m.pieta@gmail.com','6df9dc89d039c8aa87e68d5db4a06d330918d217de72418d78b48ad043fee8c1d7481ea0006340f63ab42ace33f9e4722fa319b2218acbddb6017986cd72d944','2012-06-26 17:25:10'),(9,'bobobagle@gmail.com','bobobagle@gmail.com','bobobagle@gmail.com','b8f68a795626ecd0db93856eb33ea0b9b290a8a845c786bdfc6602980cb1ad364cd34b4ad1d734bc8234db6453c5f74f846485087690b3d1a2fc6ffc59e434a3','2012-06-26 23:54:06');
/*!40000 ALTER TABLE `tg_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tg_user_group`
--

DROP TABLE IF EXISTS `tg_user_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tg_user_group` (
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`group_id`),
  KEY `group_id` (`group_id`),
  CONSTRAINT `tg_user_group_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tg_user_group_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `tg_group` (`group_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tg_user_group`
--

LOCK TABLES `tg_user_group` WRITE;
/*!40000 ALTER TABLE `tg_user_group` DISABLE KEYS */;
INSERT INTO `tg_user_group` VALUES (1,1);
/*!40000 ALTER TABLE `tg_user_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `topic`
--

DROP TABLE IF EXISTS `topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topic` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL,
  `title` varchar(255) NOT NULL,
  `creator_id` int(11) NOT NULL,
  `update_time` datetime NOT NULL,
  `logourl` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  KEY `creator_id` (`creator_id`),
  CONSTRAINT `topic_ibfk_1` FOREIGN KEY (`creator_id`) REFERENCES `tg_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topic`
--

LOCK TABLES `topic` WRITE;
/*!40000 ALTER TABLE `topic` DISABLE KEYS */;
INSERT INTO `topic` VALUES (16,'2012-12-26 13:08:02','CS 273 / OS',5,'2012-12-28 14:51:36','https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSPsE4gdHg-43dGYHCa23nxio5xlFQr6dOguD9gPCAoO7BjMhndJw'),(17,'2012-12-26 13:08:02','Hadoop Performance',5,'2012-12-26 13:08:02','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNzRJoy8K6auu9JKpm6gRwi73Pg_8eFhX8OtYGvPFL5CDb_fmi'),(18,'2012-12-26 13:08:02','CS 431 / Real-time Systems',5,'2012-12-27 01:02:18','https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRDnYoiJs3iQEmraUXuu0HGQmPPgEIFCL8Bqk3uFrLljkUMMOQ1tg'),(19,'2012-12-26 13:08:02','Niagra Fall camping',5,'2012-12-28 15:34:50','https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR9GBLKZ1rHDb2nnOoUAC7_0IE2ufGy7lMAgCcF_jX2Oey_d8zKxQ'),(20,'2012-12-26 13:08:02','Dine out Friday with the Gang',5,'2012-12-26 13:08:02','https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTIDdbe_jrejaj07KjPS5OUODJUBdJUhyDrDeIycrA7WHBJBGPi'),(21,'2012-12-26 13:08:02','Basketball Tournament',5,'2012-12-26 13:08:02','https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSAJX5LHy7O-y4DVwMqVrSd8fbdC0nvmHK-utkf9nd2o2Ax5Fc5'),(22,'2012-12-26 13:54:23','Web Monkey',5,'2012-12-26 13:54:23','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuHie03GOLozVhuQBMoBQRlYDpkmGkJz4PBvqIrTK7vOprJnmnaw');
/*!40000 ALTER TABLE `topic` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-12-28 16:14:08
