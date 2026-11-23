#!/bin/bash
docker rm -f flaskapp 2>/dev/null
docker build -t myflask .
docker run -d --name flaskapp -p 9090:9090 myflask
echo "App dispo sur http://localhost:9090"
