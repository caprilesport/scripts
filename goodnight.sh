#!/usr/bin/bash

# This script is used at the end of work, it syncs all work with google drive and shuts down if asked for (if jobs are running on the machine it is ignored)



# back up in google drive
folders=("/home/vinicp/Chem" "/home/vinicp/Documents" "/home/vinicp/physics")

for i in "${folders[@]}"
do 
cd $i 
gdrive push 

done 

# shutdown now 