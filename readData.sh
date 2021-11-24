#!/bin/bash
cd /home/pi/fresh/
echo $$ > readData.pid
exec python3 readData.py