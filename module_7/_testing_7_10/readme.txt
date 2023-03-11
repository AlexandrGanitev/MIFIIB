Запуск файла с дополнительными параметрами.

docker run -d --name myapitestingcontaier -p 80:80  api_ag
b3a9414c9d9612c4b5f73b92349328480f4f6ad8cb684377f09891e5220e135e

-d running in the background
--name gives the name to the existing container
-p port on which the api is working for this container

Checking the structure of the container by its ID.

_testing_7_10 % docker exec -ti b3a9414c9d9612c4b5f73b92349328480f4f6ad8cb684377f09891e5220e135e /bin/sh
# ls
app  requirements.txt
# cd ..
# ls
bin  boot  code  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
#
