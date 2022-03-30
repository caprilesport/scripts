#!/usr/bin/bash

# This script is used at startup, it syncs up with google drive and opens the news on firefox

# sync with back up in google drive
folders=("/home/vinicp/Chem" "/home/vinicp/Documents" "/home/vinicp/physics")

for i in "${folders[@]}"
do 
cd $i 
gdrive pull 

done 

# check cluster for completed jobs



# fire up firefox with news


