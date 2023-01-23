#!/bin/bash

count=1
while true
do


	palabra=$(cat 10_million_password_list_top_100000.txt | awk "NR==$count")
	primer_caracter=$(echo $palabra | head -c 1 )
	primer_caracter_mayuscula=$(echo $primer_caracter | tr "a-z" "A-Z")

	ultimo_caracter=$(echo $palabra | tail -c 1)
	palabra=$(echo $palabra | sed  "s/$primer_caracter/$primer_caracter_mayuscula/")
	palabra=$palabra'0'
	echo $palabra 

	if [ $count -lt 100000 ]
	then
		count=$((count+=1))
		
	else
		break
	fi
done
