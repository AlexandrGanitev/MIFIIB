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


