#!/bin/bash
source /etc/profile
Local_ip=`ip r |grep "scope link  src" |awk '{print $NF}'`
if [[ $Local_ip == *.*.*.* ]];then
        Local_ip=$Local_ip
else
        Local_ip=`ip r |grep "scope link  src" |awk '{print $9}'`
fi

echo $Local_ip >/home/finance/Shell/$Local_ip.txt
