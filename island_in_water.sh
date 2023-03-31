#!/usr/bin/env bash

if  ! [ $# -eq 1 ]; then
        echo "Please provide filename islands.txt to the shell script. Script execution :: bash island_in_water.sh islands.txt"
        exit 1  
fi

python3 island_in_water.py $1





