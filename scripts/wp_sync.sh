#!/bin/bash

/usr/bin/python3 /home/openclaw/insightginie/scripts/sync_wordpress.py

cd /home/openclaw/insightginie

git add .

git commit -m "auto sync $(date)" || exit 0

git push