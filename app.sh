#!/bin/bash
docker rm -f flaskapp 2>/dev/null
docker build -t myflask .
docker run -d --name flaskapp -p 8091:5000 myflask
echo "App dispo sur http://localhost:8091"
