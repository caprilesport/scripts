#!/bin/bash
echo "submitting CREST with '$3' solvation"
crest $1 --alpb $3 --opt --T 6 --tnmd 300 --hflip | tee $2 &
