#!/bin/bash

mv *.py ./1-100 >/dev/null 2>&1 || true

for i in {1..30}; do
    let j=$i+1
    files="${i}??.*.py"

    lo="${i}01"
    hi="${j}00"
    folder="./${lo}-${hi}"

    mkdir -p ${folder}
    mv ${files} ${folder} >/dev/null 2>&1 || true
done
