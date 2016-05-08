#!/bin/bash
rm mr1_out
rm mr1_err
echo $1 >> debug
echo $2 >> debug
echo $3 >> debug
echo $4 >> debug
source /etc/profile
hadoop fs -rm -r /postsout/total
hadoop jar /opt/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper ~/termProject/code/question-mapper.py -reducer ~/termProject/code/question-reducer.py -file ~/termProject/code/question-mapper.py -file ~/termProject/code/question-reducer.py -input /postsinput/result.txt -output /postsout/total -numReduceTasks 0  -cmdenv tag1=$1 -cmdenv tag2=$2 -cmdenv tag3=$3 -cmdenv tag4=$4  > mr1_out 2> mr1_err

