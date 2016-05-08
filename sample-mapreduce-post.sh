#!/bin/bash
DATE=$(date +"%Y%m%d%H%M")
source /etc/profile
echo "start question map-reduce mission"
hadoop fs -rm -r /sample-output/android
hadoop jar /opt/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper ~/termProject/code/question-mapper.py -reducer ~/termProject/code/question-reducer.py -file ~/termProject/code/question-mapper.py -file ~/termProject/code/question-reducer.py -input /android-sample-input/result.txt -output /sample-output/android  -cmdenv tag1=$1 -cmdenv tag2=$2 -cmdenv tag3=$3 -cmdenv tag4=$4 -numReduceTasks 2
echo "tag1: $1,tag2: $2,tag3 $3,tag4: $4"
echo "question map-reduce finished"
echo "copy to local"
rm -r ~/termProject/sampleData/mapreduce1-output/*
hadoop fs -copyToLocal /sample-output/android ~/termProject/sampleData/mapreduce1-output
echo "combine result"
cat ~/termProject/sampleData/mapreduce1-output/android/part-0000* > ~/termProject/sampleData/finalResult/accepted_answer.txt
echo "combine completed"

