  GNU nano 6.2                                              number2_v1.sh *
#!/bin/bash

# Navigate to the user's home directory:
file=~/.local/bin/number2_v1.sh
chmod +x $file
printf "\n"
echo "Granting +x permissions on the number2.sh script file"
cd ~/ and ls -l

# Creating the backup with archiving:
echo "Creating the backup with archiving..."
tar -zcvpf /archive/AG_backup-"Created on $(date +%d-%B-%Y).tar.gz" /home/skillfactory_lab/Desktop \
/home/skillfactory_lab/docker /home/skillfactory_lab/Documents /home/skillfactory_lab/PycharmProjects \
/home/skillfactory_lab/data /etc/ssh/sshd_config /etc/xrdp /etc/vsftpd.conf /var/log

#tar -zcvpf $BACKUP_DIR/AG-$DATE.tar.gz /etc/ssh/sshd_config

#tar -zcvpf $BACKUP_DIR/AG-$DATE.tar.gz /home/skillfactory_lab /etc/ssh/sshd_config /etc/xrdp /etc/vsftpd.conf /var/log

# main command:
# tar -zcvpf /[Backup_Location]/[Backup_Filename] /[User_Home_Directory_Location]