#!/bin/bash
string1=$(whoami)
string2=root
if [ string1 == string2 ]; # #так будет правильнее использовать конструкцию сравнения пользователей
then echo you are root
else echo you are not root
fi
echo Здесь изначально была ошибка присваивания, так было дано в уроке
echo 'if [ string1=string2 ]' оператор присваивал значение одной строки другой, вот и выходило всегда you are root

