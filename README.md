
2020-01-03 - andreas.kraxner@gmail.com
this script generates switch configs the examples are for hp switches
build your control file switche.csv
<switch_name>;<ip-adress>;<port-tagged-uplinks-vlans>

the switch_name must begin with swe or swc
   * swe - Edgeswitch
   * swc - Distribution Switch

example 
    swc-sepp2;10.10.10.102;A1-B8
    swe-sepp1;10.10.10.1;49-52