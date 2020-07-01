#!/usr/bin/python

'''
2020-01-03 - andreas.kraxner@gmail.com
this script generates switch configs the examples are for hp switches
build your control file switche.csv
<switch_name>;<ip-adress>;<port-tagged-vlans>

the switch_name must begin with swe or swc
   * swe - Edgeswitch
   * swc - Distribution Switch

example
    swc-sepp2;10.10.10.102;A1-B8
'''

import csv
from shutil import copyfile

#set the subnet for management ip's
ip_mgmt_subnet="255.255.252.0"

def generate_file(hostname, ipaddress, portrange, type):
    with open('basis-swconfig-' + type) as fx:
        newT = fx.read().replace('<ip_mgmt_address>', ipaddress)
        newT2 = newT.replace('<port-range>', portrange)
        newT3 = newT2.replace('<hostname>', hostname)
        newT4 = newT3.replace('<ip_mgmt_subnet>', ip_mgmt_subnet)


    with open(switch[0] + '.txt', "w") as fy:
        fy.write(newT4)
    fx.close()
    fy.close()

with open('switche.csv', mode='r') as swichtcsv:
    switchreader = csv.reader(swichtcsv, delimiter=';')
    for switch in switchreader:
        if str(switch[0]).find('swc-') != -1:
            generate_file(switch[0], switch[1], switch[2], "core")
        elif str(switch[0]).find('swd-') != -1:
            generate_file(switch[0], switch[1], switch[2], "dist")
        elif str(switch[0]).find('swe-') != -1:
            generate_file(switch[0], switch[1], switch[2], "core")
        else:
            print "the name of the switch " + switch[0] + " must begin with <swc-> or <swd-> or <swc->"

swichtcsv.close()
