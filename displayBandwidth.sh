#!/usr/bin/env bash

while true; do

# Run the delta query output to file
# snmpdelta pfsense -v2c -cg33kpfsense -Ovq -Cl .1.3.6.1.2.1.31.1.1.1.6.3 

# Tail the last line of the file, pipe into sed to strip out the common OID stamp

# UPLOAD VARIABLES
A=`(tail -n1 pfsense-iso.3.6.1.2.1.31.1.1.1.10.3 | awk '{ print $4 }')`
B=$(echo "scale=3;$A/3276800" | bc)
C=$(echo "$B*100" | bc)

# DOWNLOAD VARIABLES
N=`(tail -n1 pfsense-iso.3.6.1.2.1.31.1.1.1.6.3 | awk '{ print $4 }')`
P=$(echo "scale=3;$N/22937600" | bc)
O=$(echo "$P*100" | bc)

echo "$O,$C" | sudo python outputLED.py 
# echo 100,100 | sudo python outputLED.py

sleep 1
done



