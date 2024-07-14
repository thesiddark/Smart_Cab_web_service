/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 10.4.28-MariaDB : Database - smart_cab
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`smart_cab` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `smart_cab`;

/*Data for the table `auth_group` */

/*Data for the table `auth_group_permissions` */

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add ambulance_ driver',7,'add_ambulance_driver'),
(26,'Can change ambulance_ driver',7,'change_ambulance_driver'),
(27,'Can delete ambulance_ driver',7,'delete_ambulance_driver'),
(28,'Can view ambulance_ driver',7,'view_ambulance_driver'),
(29,'Can add ambulance_request',8,'add_ambulance_request'),
(30,'Can change ambulance_request',8,'change_ambulance_request'),
(31,'Can delete ambulance_request',8,'delete_ambulance_request'),
(32,'Can view ambulance_request',8,'view_ambulance_request'),
(33,'Can add driver',9,'add_driver'),
(34,'Can change driver',9,'change_driver'),
(35,'Can delete driver',9,'delete_driver'),
(36,'Can view driver',9,'view_driver'),
(37,'Can add driver_ request',10,'add_driver_request'),
(38,'Can change driver_ request',10,'change_driver_request'),
(39,'Can delete driver_ request',10,'delete_driver_request'),
(40,'Can view driver_ request',10,'view_driver_request'),
(41,'Can add login',11,'add_login'),
(42,'Can change login',11,'change_login'),
(43,'Can delete login',11,'delete_login'),
(44,'Can view login',11,'view_login'),
(45,'Can add user',12,'add_user'),
(46,'Can change user',12,'change_user'),
(47,'Can delete user',12,'delete_user'),
(48,'Can view user',12,'view_user'),
(49,'Can add payment_to_cab',13,'add_payment_to_cab'),
(50,'Can change payment_to_cab',13,'change_payment_to_cab'),
(51,'Can delete payment_to_cab',13,'delete_payment_to_cab'),
(52,'Can view payment_to_cab',13,'view_payment_to_cab'),
(53,'Can add payment_to_ambulance',14,'add_payment_to_ambulance'),
(54,'Can change payment_to_ambulance',14,'change_payment_to_ambulance'),
(55,'Can delete payment_to_ambulance',14,'delete_payment_to_ambulance'),
(56,'Can view payment_to_ambulance',14,'view_payment_to_ambulance'),
(57,'Can add feedback',15,'add_feedback'),
(58,'Can change feedback',15,'change_feedback'),
(59,'Can delete feedback',15,'delete_feedback'),
(60,'Can view feedback',15,'view_feedback'),
(61,'Can add complaint',16,'add_complaint'),
(62,'Can change complaint',16,'change_complaint'),
(63,'Can delete complaint',16,'delete_complaint'),
(64,'Can view complaint',16,'view_complaint'),
(65,'Can add location',17,'add_location'),
(66,'Can change location',17,'change_location'),
(67,'Can delete location',17,'delete_location'),
(68,'Can view location',17,'view_location');

/*Data for the table `auth_user` */

/*Data for the table `auth_user_groups` */

/*Data for the table `auth_user_user_permissions` */

/*Data for the table `django_admin_log` */

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'myapp','ambulance_driver'),
(8,'myapp','ambulance_request'),
(16,'myapp','complaint'),
(9,'myapp','driver'),
(10,'myapp','driver_request'),
(15,'myapp','feedback'),
(17,'myapp','location'),
(11,'myapp','login'),
(14,'myapp','payment_to_ambulance'),
(13,'myapp','payment_to_cab'),
(12,'myapp','user'),
(6,'sessions','session');

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-11-24 10:34:09.459179'),
(2,'auth','0001_initial','2023-11-24 10:34:24.577093'),
(3,'admin','0001_initial','2023-11-24 10:34:26.353610'),
(4,'admin','0002_logentry_remove_auto_add','2023-11-24 10:34:26.403877'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-11-24 10:34:26.448384'),
(6,'contenttypes','0002_remove_content_type_name','2023-11-24 10:34:27.258059'),
(7,'auth','0002_alter_permission_name_max_length','2023-11-24 10:34:29.295948'),
(8,'auth','0003_alter_user_email_max_length','2023-11-24 10:34:29.512513'),
(9,'auth','0004_alter_user_username_opts','2023-11-24 10:34:29.560784'),
(10,'auth','0005_alter_user_last_login_null','2023-11-24 10:34:30.972791'),
(11,'auth','0006_require_contenttypes_0002','2023-11-24 10:34:31.021090'),
(12,'auth','0007_alter_validators_add_error_messages','2023-11-24 10:34:31.102883'),
(13,'auth','0008_alter_user_username_max_length','2023-11-24 10:34:31.260710'),
(14,'auth','0009_alter_user_last_name_max_length','2023-11-24 10:34:31.420277'),
(15,'auth','0010_alter_group_name_max_length','2023-11-24 10:34:31.690926'),
(16,'auth','0011_update_proxy_permissions','2023-11-24 10:34:31.736157'),
(17,'auth','0012_alter_user_first_name_max_length','2023-11-24 10:34:31.869292'),
(18,'myapp','0001_initial','2023-11-24 10:34:55.978350'),
(19,'sessions','0001_initial','2023-11-24 10:34:56.765569'),
(20,'myapp','0002_user_post','2023-12-05 03:43:15.773520'),
(21,'myapp','0003_ambulance_driver_status','2023-12-05 04:46:27.413484'),
(22,'myapp','0004_location','2023-12-21 05:58:47.144156'),
(23,'myapp','0005_ambulance_driver_vphoto','2023-12-22 08:53:01.866775');

/*Data for the table `django_session` */

/*Data for the table `myapp_ambulance_driver` */

insert  into `myapp_ambulance_driver`(`id`,`name`,`email`,`phone`,`gender`,`photo`,`proof`,`dob`,`place`,`post`,`pin`,`vreg_no`,`district`,`LOGIN_id`,`status`,`vphoto`) values 
(1,'driver','mdkjd','cjhbdc','mndcmnd','','','2023-12-21','nsdbc','nbdcv','sgch','KL 17 F0987','gdhg',6,'approved','no'),
(2,'am','amb@gmail.com','8363535252','Female','/media/ambulance/photo/20231222-150250.jpg','/media/ambulance/proof/20231222-1502501.jpg','2023-12-22','bdhdhf','bdbd','654326','KL 12 M 0987','bdbd',20,'pending','/media/ambulance/vphoto/20231222-150250.jpg'),
(3,'ambula','amb@gmail.com','8363535252','Female','/media/ambulance/photo/20231222-150250.jpg','/media/ambulance/proof/20231222-1502501.jpg','2023-12-22','bdhdhf','bdbd','654326','KL 12 M 0987','bdbd',21,'pending','/media/ambulance/vphoto/20231222-150250.jpg'),
(4,'ambu','amb@gmail.com','8363535252','Female','/media/ambulance/photo/20231222-150250.jpg','/media/ambulance/proof/20231222-1530591.jpg','2023-12-22','bdhdhf','bdbd','654378','KL 12 M 0987','bdbd',22,'approved','/media/ambulance/vphoto/20231222-150250.jpg'),
(5,'ambulance','am@yahoo.com','9876515278','Female','/media/ambulance/photo/20240105-100959.jpg','/media/ambulance/proof/20240105-1009591.jpg','2024-01-05','kozhikode','post','624415','KL 18 B 0986','post',25,'pending','/media/ambulance/vphoto/20240105-100959.jpg'),
(6,'ambulance','am@yahoo.com','9876515278','Male','/media/ambulance/photo/20240105-100959.jpg','/media/ambulance/proof/20240105-1009591.jpg','2024-01-05','kozhikode','post','624415','KL 18 B 0986','post',23,'pending','/media/ambulance/vphoto/20240105-100959.jpg'),
(7,'ambulance','am@yahoo.com','9876515278','Male','/media/ambulance/photo/20240105-100959.jpg','/media/ambulance/proof/20240105-1009591.jpg','2024-01-05','kozhikode','post','624415','KL 18 B 0986','post',24,'approved','/media/ambulance/vphoto/20240105-100959.jpg');

/*Data for the table `myapp_ambulance_request` */

insert  into `myapp_ambulance_request`(`id`,`date`,`source`,`destination`,`status`,`AMBULANCE_DRIVER_id`,`USER_id`) values 
(1,'2023-12-21','wayanad','kozhikode','pending',1,7),
(2,'2024-01-08','kkd','knr','pending',7,7),
(3,'2024-01-08','kkd','knr','pending',7,7),
(4,'2024-01-08','kkd','knr','pending',7,7),
(5,'2024-01-08','kkd','knr','pending',7,7);

/*Data for the table `myapp_complaint` */

insert  into `myapp_complaint`(`id`,`date`,`complaint`,`status`,`reply`,`USER_id`) values 
(1,'2023-12-20','vdhdjdjdj gdhdhd','pending','pending',7);

/*Data for the table `myapp_driver` */

insert  into `myapp_driver`(`id`,`name`,`email`,`phone`,`gender`,`photo`,`proof`,`vphoto`,`dob`,`place`,`post`,`pin`,`vnumber`,`district`,`status`,`LOGIN_id`) values 
(1,'driver','d@gmail.com','9876543210','Male','/driver/photo/20231205-174031.jpg','/driver/proof/20231205-1740311.jpg','/driver/vphoto/20231205-1740312.jpg','2023-12-05','vshshs','vsvs','678890','KL 19 U 3330','vsvs','pending',9),
(2,'driver','d@gmail.com','9876543210','Male','/driver/photo/20231205-174031.jpg','/driver/proof/20231205-1740311.jpg','/driver/vphoto/20231205-1740312.jpg','2023-12-05','vshshs','vsvs','678890','KL 19 U 3330','vsvs','approved',1),
(3,'driver','d@gmail.com','9876543210','Male','/driver/photo/20231205-174031.jpg','/driver/proof/20231205-1740311.jpg','/driver/vphoto/20231205-1740312.jpg','2023-12-05','vshshs','vsvs','678890','KL 19 U 3330','vsvs','pending',10),
(4,'raju','s@gmail.com','7363337123','Others','/media/driver/photo/20231207-155857.jpg','/media/driver/proof/20231207-1558581.jpg','/media/driver/vphoto/20231207-1558582.jpg','2023-12-07','hshss','svvss','637484','KL 18 U 2033','svvss','approved',17),
(5,'saji','s@gmail.com','7363337123','Others','/media/driver/photo/20231207-155857.jpg','/media/driver/proof/20231207-1558581.jpg','/media/driver/vphoto/20231207-1558582.jpg','2023-12-07','hshss','svvss','637484','KL 18 U 2033','svvss','pending',16),
(6,'saji','s@gmail.com','7363337123','Male','/media/driver/photo/20231207-161738.jpg','/media/driver/proof/20231207-1616521.jpg','/media/driver/vphoto/20231207-1558582.jpg','2023-12-01','hshss','svvss','637484','KL 18 U 2033','svvss','approved',18);

/*Data for the table `myapp_driver_request` */

insert  into `myapp_driver_request`(`id`,`date`,`source`,`destination`,`status`,`DRIVER_id`,`USER_id`) values 
(1,'2023-12-13','kozhikode','wayanad','approved',6,7),
(2,'2023-12-19','kozhikode','vadakara','rejected',6,7),
(3,'2024-01-05','kozhikode','vadakara','approved',6,2);

/*Data for the table `myapp_feedback` */

insert  into `myapp_feedback`(`id`,`date`,`Feed_back`,`USER_id`) values 
(1,'2023-12-21','sdfgvv',7);

/*Data for the table `myapp_location` */

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'d','d','driver'),
(2,'u','u','user'),
(3,'','','user'),
(4,'','','user'),
(5,'u@gmail','','user'),
(6,'am','1','ambulance'),
(7,'','','user'),
(8,'u@gmail','567','user'),
(9,'d@gmail.com','1','pending'),
(10,'d@gmail.com','123','pending'),
(11,'dr','1','pending'),
(12,'us@gmail','987','user'),
(13,'m@gmail','246','user'),
(14,'achu@gmail','12345','user'),
(15,'r@gmail.com','987','user'),
(16,'s12@gmail.com','8902','pending'),
(17,'s1@gmail.com','8908','pending'),
(18,'ss@gmail.com','1','driver'),
(19,'am@gmail.com ','7890','user'),
(20,'amb@gmail.com','10','pending'),
(21,'amb@gmail.com','9','pending'),
(22,'amb@gmail.com','0','ambulance'),
(23,'am@yahoo.com','10','pending'),
(24,'am@yahoo.com','18','ambulance'),
(25,'am@yahoo.com','1','ambulance');

/*Data for the table `myapp_payment_to_ambulance` */

/*Data for the table `myapp_payment_to_cab` */

/*Data for the table `myapp_user` */

insert  into `myapp_user`(`id`,`name`,`email`,`phone`,`gender`,`photo`,`dob`,`place`,`pin`,`district`,`LOGIN_id`,`post`) values 
(1,'','u@gmail','','Male','/media/user/20231205-143706.jpg','2023-12-05','','','',5,''),
(2,'user','u@gmail','82722222','Male','/media/user/20231205-172232.jpg','2023-12-05','hshss','672828','shhss',8,'shhss'),
(3,'use','us@gmail','8836363667','Female','/user/20231206-165112.jpg','2023-12-06','hdhd','625278','hdjd',12,'hdjd'),
(4,'maya','m@gmail','9524252729','Female','/user/20231206-165407.jpg','2023-12-01','bsns','651431','hddh',13,'hddh'),
(5,'achu','achu@gmail','862625555','Female','/media/user/20231206-165740.jpg','2023-12-02','gdgsh','726262','gdhdd',14,'gdhdd'),
(6,'ramya','r@gmail.com','9716151526','Female','/media/user/20231207_152622.jpg','2023-12-07','sbs','636362','bshs',15,'bshs'),
(7,'amaya','am@gmail.com ','6789012345','Female','/media/user/20231213-153949.jpg','2023-12-13','kkd','641577','gdhdd',19,'gdhdd');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
