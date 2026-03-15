#!/bin/bash
cd /home/thecataclysmo/discordbot
source bot-env/bin/activate
while true; do
	python3 catapi.py
	echo "Bot crashed, restarting..."
	sleep 5
done
