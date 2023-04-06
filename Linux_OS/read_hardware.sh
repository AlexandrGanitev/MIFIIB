#!/bin/bash

cat servers.txt | grep -v CPU | while read servername cpu ram ip
do
   echo $ip $servername
done
