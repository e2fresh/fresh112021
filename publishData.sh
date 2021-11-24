#!/bin/bash
cd /home/pi/fresh/
echo $$ > publishData.pid
exec python3 publishData1.py