#!/bin/bash
cat users.txt | awk '{print$1}' | xargs -n 1 useradd -m
# this line above creates three users from users.txt file, prints the patters (user_x) and sends the output to xargs
# which iterates line by line and adds these uses to the system.
for iterator in `cat users.txt | awk '{print$1}'`
# we put the `-quotes because we use the regular ones in the awk command
do 
	touch /home/$iterator/skillfactory && echo -e "Hello from Skillfactory" > /home/$iterator/skillfactory
done
# for loop creates by iterating (iterator) the home directories and passes the message to each user, creats file skillfactory
# and add Hello message to each.
# Output:
# user_1@Linux:/home/skillfactory_lab/.local/bin$ cd ~/
# user_1@Linux:~$ ls
# skillfactory
# user_1@Linux:~$ cat skillfactory
# Hello from Skillfactory
# user_1@Linux:~$ 

# search the strings inside of the file with sed, then using awk we are searchin for a divider : and pass to xargs
# that runs the command chsh (change shell) to /bin/bash:
sed -n '/user_[1-3]/p' /etc/passwd | awk -F ":" '{print$1}' | xargs -n 1 chsh -s /bin/bash
# Output:
# user_1:x:1003:1004::/home/user_1:/bin/bash
# user_2:x:1004:1005::/home/user_2:/bin/bash
# user_3:x:1005:1006::/home/user_3:/bin/bash
chpasswd < pass.txt
# this command passes the password to chpasswd command in a required format, otherwise we need to pass each user
# this way chpasswd user:password.

# changing the passwords in bulk,logging in as user_2, Output:
# skillfactory_lab@Linux:~/.local/bin$ su user_2
# Password: 
# user_2@Linux:/home/skillfactory_lab/.local/bin$ 
