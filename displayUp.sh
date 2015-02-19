#!/usr/bin/env bash

while true; do

# Run the delta query output to file
# snmpdelta pfsense -v2c -cg33kpfsense -Ovq -Cl .1.3.6.1.2.1.31.1.1.1.6.3 

# Tail the last line of the file, pipe into sed to strip out the common OID stamp

# N=`(tail -n1 pfsense-iso.3.6.1.2.1.31.1.1.1.6.3 | sed 's/iso\.3\.6\.1\.2\.1\.31\.1\.1\.1\.6\.3 \/1 sec: //' | printf "%d")`
N=`(tail -n1 pfsense-iso.3.6.1.2.1.31.1.1.1.6.3 | awk '{ print $4 }')`
P=$N/22937600
Q= `echo $P | bc`
echo $N 
echo $P
echo $Q
sleep 5
done



