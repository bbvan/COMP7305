#!/bin/bash
DATE=$(date +"%Y%m%d%H%M")
source /etc/profile
echo "second map-reduce start"                                            
hadoop fs -rm -r /sample-output2/android 
hadoop jar /opt/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper ~/termProject/code/answer-mapper.py -reducer ~/termProject/code/answer-reducer.py -file ~/termProject/code/answer-mapper.py -file ~/termProject/code/answer-reducer.py -input /android-sample-input/result.txt -output /sample-output2/android -numReduceTasks 2 -file ~/termProject/sampleData/finalResult/accepted_answer.txt
echo "second map-reduce finished"
 
