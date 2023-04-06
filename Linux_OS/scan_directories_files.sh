#!/bin/bash
for file in "$@" #тут мы пользуемся оператором $@ - т.е. все значения, переданные параметром, будут
# восприминаться отдельно, в качестве примера /etc/*
do 
if [ -d "$file" ]
then 
echo "$file - директория"
elif [ -f "$file" ]
then
echo "$file -файл"
fi
done
# запуск скрипта: sh scan_directories_files.sh /etc/*
