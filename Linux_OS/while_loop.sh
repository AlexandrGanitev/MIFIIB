#!/bin/bash
i=$1
while [ $i -lt 5 ]
do
echo "Number: $i"
 ((i++))
 if [[ "$i" == '4' ]]; then
break
fi
done
echo 'я посчитал до 4'

echo 'скрипт можно запустить так:'
echo './while_loop.sh 2'
echo 'sh while_loop.sh 2'
echo 'bash while_loop.sh 2'
echo 'обязательно дайте разрешение на выполнение скрипта - "chmod +x file_name"'
