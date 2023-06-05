It was about 3 months, since I set up the docker with mysql and php. Adding some steps.

1. Navigate to the directory of the Dockerfile and YAML, build the php apache:
    docker build -t ganitev2:latest .
2. Compose the containers:
    docker-compose up
3. Log in to mysqlclient_ag, and add the instruments to the DB:
    docker exec -ti mysqlclient_ag /bin/bash (в случае этого контейнера будет именно /bin/bash)
    # mysql -h 172.18.0.2 -u root -padmin (here find the IP of the container from Visual Code Studio, go to Docker,
    right-click on mysql5.7->Inspect->scroll to the bottom and find the IP: 172.18.0.x)
    mysql> show databases;
    mysql> use instruments;
    mysql> select*from guitars;
    mysql>
        INSERT INTO guitars (id, brand, model) VALUES
        ->
            ('1', 'ADMIRA', 'ARTISTA'), ('2', 'TAYLOR', 'CE110'), ('3', 'MARTIN', 'D28'), ('4', 'OVATION', 'ADAMAS'), ('5', 'YAMAHA', 'FG800'), ('6', 'EPIPHONE', 'DR-100'), ('7', 'TAKAMINE', 'P3NY'), ('8', 'MARTIN', 'SC-13E'), ('9', 'MATON', 'SRS');
    mysql> exit (or ctrl-d)

    If the DB instruments doesn't exits, copy and paste the following text:

    CREATE DATABASE IF NOT EXISTS instruments;
CREATE USER IF NOT EXISTS 'user'@'%'
IDENTIFIED BY 'password';
GRANT SELECT,UPDATE,INSERT ON instruments.* TO 'user'@'%';
FLUSH PRIVILEGES;

USE instruments;

CREATE TABLE IF NOT EXISTS guitars (
    id INT(10) NOT NULL,
    brand VARCHAR(20) NOT NULL,
    model VARCHAR(40) NOT NULL,
    PRIMARY KEY (ID)
  );

Then do INSERT part...

4. Check and refresh the page on http://localhost:8080, the data should be listed on it. PHP will pull the data from DB now.
