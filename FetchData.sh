#!/bin/bash

Pre=$1
Pos=$2

#Pre=5
#Pos=100

python -W ignore /var/www/html/FetchData.py ${Pre} ${Pos}

#python -W ignore /var/www/html/FetchData.py 5 100

cd Output
rm -f Data.zip
zip -r Data.zip *.mseed 1>/dev/null
chmod 777 Data.zip
rm -f *.mseed
cd ..
