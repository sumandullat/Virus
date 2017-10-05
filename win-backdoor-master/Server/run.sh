#!/bin/bash
echo "Enter the client IP: ";
read address;
netcat $address 6996;
