It was about 3 months, since I set up the docker with mysql and php. Adding some steps.

1. Navigate to the directory of the Dockerfile and YAML, build the php apache:
    docker build -t ganitev2:latest .
2. Compose the containers:
    docker-compose up
3. Log in to mysqlclient_ag, and add the instruments to the DB:
    docker exec -ti mysqlclient_ag /bin/bash
    # mysql -h 172.18.0.2 -u root -padmin (here find the IP of the container from Visual Code Studio, check notes)
    mysql> show databases;
    mysql> use instruments;
    mysql> select*from guitars;
    mysql> INSERT INTO guitars (id, brand, model) VALUES
        -> ('1', 'ADMIRA', 'ARTISTA'),
        ......);
    mysql> exit (or ctrl-d)
4. Check and refresh the page on http://localhost:8080, the data should be listed on it. PHP will pull the data from DB now.
