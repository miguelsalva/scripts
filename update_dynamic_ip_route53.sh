#!/bin/sh
#
# FILE: update_dynamic_ip_route53.sh
# AUTHOR: Miguel Salvá
# ABSTRACT: This script request the current external IP address to the ipify API and updates it on the AWS Route53 service
#
# This script requires the AWS CLI installed and the $DOMAIN and $HOSTED_ZONE variables defined to run 


DOMAIN=""  # AWS domain to be updated
HOSTED_ZONE=""  # AWS hosted zone of the domain to be updated

JSON_FILE="update_route53.json"
IP=$(curl -s https://api.ipify.org)


echo "The public IP address is: $IP"

echo "{" > $JSON_FILE
echo "            "\""Comment"\"": "\""UPSERT a record "\""," >> $JSON_FILE
echo "            "\""Changes"\"": [{" >> $JSON_FILE
echo "            "\""Action"\"": "\""UPSERT"\""," >> $JSON_FILE
echo "                        "\""ResourceRecordSet"\"": {" >> $JSON_FILE
echo "                                    "\""Name"\"": "\""$DOMAIN"\""," >> $JSON_FILE
echo "                                    "\""Type"\"": "\""A"\""," >> $JSON_FILE
echo "                                    "\""TTL"\"": 300," >> $JSON_FILE
echo "                                 "\""ResourceRecords"\"": [{ "\""Value"\"": "\""$IP"\""}]" >> $JSON_FILE
echo "}}]" >> $JSON_FILE
echo "}" >> $JSON_FILE

aws route53 change-resource-record-sets --hosted-zone-id $HOSTED_ZONE --change-batch file://$JSON_FILE
echo "The domain $DOMAIN has been successfully updated" 
