#!/bin/sh

if [ $1 == "start_server" ];then
    bgmi install > /dev/null
    bgmi config ARIA2_RPC_TOKEN ${ARIA2_TOKEN} > /dev/null
    bgmi config ADMIN_TOKEN ${BGMI_TOKEN} > /dev/null

    exec bgmi_http
else
    exec bgmi $@
fi