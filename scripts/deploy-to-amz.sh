#!/bin/sh

file=$1
msg=$2

#cd /projects/Jminee
#git commit $file -m $msg
git push
ssh -i ~/.ssh/jminee.pem ubuntu@107.20.147.56 'cd /projects/Jminee; sudo su jdev git pull'
#cd - 
