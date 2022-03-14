#!/bin/bash
#
#
timestamp="$(date +"%Y-%m-%d - %H.%M.%S")"
logNamed="log$timestamp.pcap"
#sudo -S <<< Labatus2022 whsniff -c 11 > logNamed
#
#
echo Starting recording of ZigBee-traffic through Wireshark
echo Labatus2022 | sudo -S whsniff -c 11 > $logNamed && kill
echo \n Finished
exit
