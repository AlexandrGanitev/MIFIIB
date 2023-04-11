#!/bin/bash
if ping -c 2 8.8.8.8
then echo "интернет есть"
else echo "интернета нет"
fi
