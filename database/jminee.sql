-- MySQL dump 10.13  Distrib 5.5.22, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: jminee
-- ------------------------------------------------------
-- Server version	5.5.22-0ubuntu1

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
-- Table structure for table `member_message`
--

DROP TABLE IF EXISTS `member_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member_message` (
  `user_name` varchar(255) NOT NULL,
  `message_id` int(11) NOT NULL,
  `read` tinyint(1) DEFAULT NULL,
  `delete` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`user_name`,`message_id`),
  KEY `message_id` (`message_id`),
  CONSTRAINT `member_message_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `tg_user` (`user_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `member_message_ibfk_2` FOREIGN KEY (`message_id`) REFERENCES `message` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_message`
--

LOCK TABLES `member_message` WRITE;
/*!40000 ALTER TABLE `member_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `member_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_topic`
--

DROP TABLE IF EXISTS `member_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member_topic` (
  `user_name` varchar(255) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `role` varchar(2) NOT NULL,
  `local_title` varchar(255) NOT NULL,
  `delete` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`user_name`,`topic_id`),
  KEY `topic_id` (`topic_id`),
  CONSTRAINT `member_topic_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `tg_user` (`user_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `member_topic_ibfk_2` FOREIGN KEY (`topic_id`) REFERENCES `topic` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_topic`
--

LOCK TABLES `member_topic` WRITE;
/*!40000 ALTER TABLE `member_topic` DISABLE KEYS */;
INSERT INTO `member_topic` VALUES ('bachbui@gmail.com',3,'r','CS431 Database',0),('bachbui@gmail.com',4,'r','CS73 Algorithm',0),('robert.m.pieta@gmail.com',5,'c','Test',0),('robert.m.pieta@gmail.com',7,'r','Hadoop 101',0),('testuser',1,'c','Thiller book club',0),('testuser',2,'c','Soccer club',0),('testuser',3,'c','CS431 Database',0),('testuser',4,'c','CS73 Algorithm',0),('testuser',6,'c','Performance 101',0),('testuser',7,'c','Hadoop 101',0);
/*!40000 ALTER TABLE `member_topic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `message` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime DEFAULT NULL,
  `subject` varchar(255) NOT NULL,
  `content` varchar(5000) DEFAULT NULL,
  `topic_id` int(11) DEFAULT NULL,
  `creator_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  KEY `topic_id` (`topic_id`),
  KEY `creator_name` (`creator_name`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`topic_id`) REFERENCES `topic` (`uid`),
  CONSTRAINT `message_ibfk_2` FOREIGN KEY (`creator_name`) REFERENCES `tg_user` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,'2012-06-26 04:19:42','Homework 2','blahblah',3,'testuser'),(2,'2012-07-22 22:04:39','Distributed File System','blahblah',7,'testuser');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
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
  `time` datetime DEFAULT NULL,
  `title` varchar(255) NOT NULL,
  `creator_name` varchar(255) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`uid`),
  KEY `creator_name` (`creator_name`),
  CONSTRAINT `topic_ibfk_1` FOREIGN KEY (`creator_name`) REFERENCES `tg_user` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topic`
--

LOCK TABLES `topic` WRITE;
/*!40000 ALTER TABLE `topic` DISABLE KEYS */;
INSERT INTO `topic` VALUES (1,'2012-06-26 04:06:51','Thiller book club','testuser',NULL),(2,'2012-06-26 04:08:33','Soccer club','testuser',NULL),(3,'2012-06-26 04:10:55','CS431 Database','testuser',NULL),(4,'2012-06-26 04:11:21','CS73 Algorithm','testuser',NULL),(5,'2012-07-18 22:21:09','Test','robert.m.pieta@gmail.com',NULL),(6,'2012-07-22 21:31:29','Performance 101','testuser',NULL),(7,'2012-07-22 21:33:53','Hadoop 101','testuser',NULL);
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

-- Dump completed on 2012-12-22 19:29:26
