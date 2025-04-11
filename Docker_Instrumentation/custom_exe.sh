#!/bin/bash
while :; do
    curl http://localhost:5001/
    sleep $((RANDOM % 200))
done

