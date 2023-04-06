#!/bin/bash
string1=$(whoami)
string2=root
if [ string1=string2 ] # #так будет правильнее использовать конструкцию сравнения пользователей
then echo you are root
else echo you are not root
fi
