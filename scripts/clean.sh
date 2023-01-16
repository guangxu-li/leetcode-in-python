#!/bin/bash

for i in {1..25}; do
    let j=$i+1
    files="${i}??.*.py"

    lo="${i}01"
    hi="${j}00"
    folder="./${lo}-${hi}"

    mv ${files} ${folder} >/dev/null 2>&1 || true
done

mv *.py ./1-100 >/dev/null 2>&1 || true
