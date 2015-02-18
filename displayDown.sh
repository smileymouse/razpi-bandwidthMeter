#!/usr/bin/env bash

rm pfsense-iso.3.6.1.2.1.31.1.1.1.6.3
snmpdelta pfsense -v2c -cg33kpfsense -Ovq -Cl .1.3.6.1.2.1.31.1.1.1.6.3 

tail -n1 pfsense-iso.3.6.1.2.1.31.1.1.1.6.3 |
sed 's/iso\.3\.6\.1\.2\.1\.31\.1\.1\.1\.6\.3 \/1 sec: //'

Kill
# DOWNSTRING = $(`tail -n1 pfsense-iso.3.6.1.2.1.31.1.1.1.6.3`)
# CROP = $(`sed 's/iso\.3\.6\.1\.2\.1\.31\.1\.1\.1\.6\.3 \/1 sec: //')



