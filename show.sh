#!/bin/bash
source /etc/profile
rm -rf android/
hadoop fs -get /sample-output2/android .
cat android/part* > result.txt
cat result.txt


