#!/bin/bash
rm pig_out
rm pig_err
source /etc/profile 
hadoop fs -rm -r -f /pig_output
/pig-0.15.0/bin/pig -x mapreduce ~/new.pig > pig_out 2> pig_err 
rm -rf ~/termProject/sampleData/finalResult/pig_output
hadoop fs -get /pig_output/ ~/termProject/sampleData/finalResult
cat ~/termProject/sampleData/finalResult/pig_output/part* | uniq > ~/termProject/sampleData/finalResult/unique
sort -n -r ~/termProject/sampleData/finalResult/unique > ~/termProject/sampleData/finalResult/sorted
curl -XDELETE '10.42.0.100:9200/logstash-users'
head -n 20 ~/termProject/sampleData/finalResult/sorted > ~/termProject/sampleData/finalResult/users






