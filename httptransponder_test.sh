#!/bin/sh
#
# FILE: httptransponder_test.sh
# AUTHOR: Miguel Salvá
# ABSTRACT: This script tests the script httptransponder.py for all the available HTTP status codes through the httpbin.org request & response service

./httptransponder.py http://httpbin.org/status/100%2C101%2C102%2C103%2C200%2C201%2C202%2C203%2C204%2C205%2C206%2C207%2C208%2C226%2C300%2C301%2C302%2C303%2C304%2C305%2C306%2C307%2C308%2C400%2C401%2C402%2C403%2C404%2C405%2C406%2C407%2C408%2C409%2C410%2C411%2C412%2C413%2C414%2C415%2C416%2C417%2C418%2C421%2C422%2C423%2C424%2C425%2C426%2C428%2C429%2C431%2C451%2C500%2C501%2C502%2C503%2C504%2C505%2C506%2C507%2C508%2C510%2C511
