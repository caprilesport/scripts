#!/bin/bash

# this script goes in each node of our cluster and prints out some information regarding each node
# TODO (vinicius): add more info, for example free space for storage and related.
# TODO (vinicius): leave this as a sysadmin file in the lab github
# TODO (vinicius): use awk to better format output (maybe in tabls?)

# usage: 

# cinfo temp
# cinfo RAM

nodes=( "elara" "leda" "euante" "amalteia" "himalia" "carme" "helique" "cilene" "ortosia" "euporia" "io" "harpalique" "iocasta" "ganimedes" "tebe" "praxidique" "arque" "lisiteia" "metis" "adrasteia" "carpo" )

# TEMP 

# for i in {0..200000..2}
#    do 
#      sensors
#      sleep 1
#      clear
#    done

# RAM

for i in "${nodes[@]}"; 

# if $1 == temperature do: 


# if $1 == totalmemory
do 
    echo "Total memory for $i" 
    ssh $i "grep MemTotal /proc/meminfo" 2>dev/null
done 
