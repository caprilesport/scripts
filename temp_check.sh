#!/bin/bash 

# quick script that checks temperature 

for i in {0..200000..2}
   do 
     sensors
     sleep 1
     clear
   done
