Note: The point of this minikube-hw rebuilding is the advise from Konstantine to create the Docker image
as one file versus three, I created prior.

Source used: https://doc4dev.com/en/create-a-web-site-php-apache-mysql-in-5-minutes-with-docker/

1. Creating the docker-compose.yml file.
We find two services, which represent our two containers:
A. php-apache, will be accessible from port 80 of our machine which is the default HTTP port.
The site will therefore be directly accessible from localhost. It declares that all your code,
available in the “app” folder, will then be mapped to the root of the apache server, which
is “/var/www/html”. Finally, the build part will define the Apache and PHP installation
process, which will be in the Dockerfile of the “build/php” directory, which we will detail just after.

B. mysql, will be accessible from port 3306 of our machine which is the default port of MySQL.
The site will therefore be directly accessible from localhost. The build part will define the
MySQL installation process, which will be in the Dockerfile of the build/mysql directory.
Two variables are declared and will be executed during the installation of MySQL.
MYSQL_ROOT_PASSWORD sets the root account password, MYSQL_DATABASE the default database.
It will be created if it does not exist when the container is launched. A volume is also
created in order to make the data persistent, and thus not to lose the database data once
the container is shut down.

2. Creating the Dockerfile for php in build/php/Dockerfile
We will simply tell Docker to fetch the existing php-apache image, which therefore contains apache and PHP at version 8.1.

Finally, we install the MySqli, PDO and PDO_MySQL extensions in PHP, which will be very useful for us to connect to our database.

3. Creating Dockerfile for Mysql in build/mysql/Dockerfile
Here the same operation, we ask Docker to retrieve the latest version of MySQL from the existing image.
Then, we make a change of rights on the “/var/lib/mysql” directory of the container that will be created,
in order to allow PHP to connect to it.

The configuration is now finished (and yes, already!). We can still, before launching the build,
add a simple index.php file in the “app” folder, just to check that everything works well.
Without originality, I suggest this one:
app/index.php
<?php

echo 'Hello world!';

4. Site building and testing
A. So we have confirmation that Apache and PHP are active. The first container therefore does the job well. We will therefore now, to go around the subject, check that the MySQL container is indeed active, and that the first can connect to it.

We are going to do this by connecting to MySQL from our terminal, to insert some data into a table that we are going to create, then try to display this same data from our index.php.

You need the name of your MySQL container to get started. Nothing could be simpler: Execute the command

$ docker ps --format '{{.Names}}'
in a terminal. Copy the output that mentions the word “mysql”. Then, we will perform this sequence of commands to initialize our dataset:
Or alternatively, check with command: docker container ls -a

Start container (mysql, can be done by docker-compose up and using another terminal) and connect to it:
    docker exec -ti  minikube-hw-mysql-1 /bin/bash
    or docker exec -ti  minikube-hw-mysql-1 bash

    bash-4.4# mysql -uroot -pDB_w31coMe! (log in to mysql)
mysql> use instruments;
Database changed
            Creating database:
mysql> CREATE DATABASE IF NOT EXISTS instruments;
Query OK, 1 row affected (0.01 sec)

mysql> CREATE USER IF NOT EXISTS 'user@'%'
    -> IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.01 sec)

mysql> GRANT SELECT,UPDATE,INSERT ON instruments.* TO 'user'@'%';
Query OK, 0 rows affected (0.00 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.01 sec)

mysql>
mysql> USE instruments;
Database changed
mysql>
mysql> CREATE TABLE IF NOT EXISTS guitars (
    ->     id INT(10) NOT NULL,
    ->     brand VARCHAR(20) NOT NULL,
    ->     model VARCHAR(40) NOT NULL,
    ->     PRIMARY KEY (ID)
    ->   );
Query OK, 0 rows affected, 1 warning (0.02 sec)
            Inserting the data into the new database:

Здесь важно после создания базы, вставить первую строку, а потом осталъные во избежание ошибок с добавлением.

mysql> INSERT INTO guitars (id, brand, model) VALUES
    -> ('1', 'ADMIRA', 'ARTISTA');
Query OK, 1 row affected (0.02 sec)

mysql> INSERT INTO guitars (id, brand, model) VALUES
    -> ('2', 'TAYLOR', 'CE110'), ('3', 'MARTIN', 'D28'), ('4', 'OVATION', 'ADAMAS'), ('5', 'YAMAHA', 'FG800'), ('6', 'EPIPHONE', 'DR-100'), ('7', 'TAKAMINE', 'P3NY'), ('8', 'MARTIN', 'SC-13E'), ('9', 'MATON', 'SRS');
Query OK, 8 rows affected (0.01 sec)
Records: 8  Duplicates: 0  Warnings: 0

mysql> exit
    exit (to get out of bash

Example of my init.sql:

CREATE DATABASE IF NOT EXISTS instruments;
CREATE USER IF NOT EXISTS 'root'@'%'
IDENTIFIED BY 'password';
GRANT SELECT,UPDATE,INSERT ON instruments.* TO 'root'@'%';
FLUSH PRIVILEGES;

USE instruments;

CREATE TABLE IF NOT EXISTS guitars (
    id INT(10) NOT NULL,
    brand VARCHAR(20) NOT NULL,
    model VARCHAR(40) NOT NULL,
    PRIMARY KEY (ID)
  );

B. Modifying index.php
Нужно зайти на вебсервер:
    kubectl exec -ti webapp-deployment-575c58b769-sjnnc bash
установитъ nano/vim, вставить index.php, чтобы сайт работал.
                index.php:
<html lang="en">

<head>
    <title>Our Best Instruments</title>
    <link rel="stylesheet" href="style.css" type="text/css" />
</head>

<body>
    <h1  align= "center">Accoustic Instruments</h1>
    <table style="border:1px solid black;margin-left:auto;margin-right:auto;">
        <tr>
            <th>ID</th>
            <th>BRAND</th>
            <th>MODEL</th>
        </tr>
        <?php
        $host = "mysql-service"; # here it's important to put the variables out of new mysqli line below:
        $dbname = "instruments";
        $username = "root";
        $password = "DB_w31coMe!";

        $mysqli = new mysqli($host, $username, $password, $dbname);
        $result = $mysqli->query("SELECT * FROM guitars");
        foreach ($result as $row) {
            echo "<tr><td>{$row['id']}</td><td>{$row['brand']}</td><td>{$row['model']}</td></tr>";
        }
        ?>
    </table>
    <?php
    phpinfo();
    ?>
</body>

</html>


