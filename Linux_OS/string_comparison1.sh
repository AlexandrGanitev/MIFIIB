#!/bin/bash
string1="verylongnamelongname"
string2="shortname"
if [ $string1\< "$string2" ]
then echo "длина вашего имени короче переменной string1"
else echo "длина вашего имени длиннее переменной string2"
fi

