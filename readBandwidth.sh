rm pfsense*
# Mouse -- update to match the PDX LAN community / OID's of choice.  Take note of the log files made when running this.
snmpdelta pfsense -v2c -cg33kpfsense -Ovq -Cl .1.3.6.1.2.1.31.1.1.1.6.3 .1.3.6.1.2.1.31.1.1.1.10.3
