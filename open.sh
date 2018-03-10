#!/usr/bin/env sh

if [ -z "$1" ]; then
    echo "usage: open.sh filename"
else
    if [ -f "$1/$1.circ" ]; then
        java -jar ../logisim-evolution.jar -questa no $1/$1.circ
    else
        echo "error: $1 not found"
    fi
fi