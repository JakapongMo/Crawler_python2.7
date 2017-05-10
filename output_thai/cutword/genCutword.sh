#!/bin/bash

#java LongLexTo [input text file] [output csv file]

max=9
# javac LongLexTo.java
for i in `seq 1 $max`
do
	java LongLexTo "sample/sample$i.txt" "cutword$i.csv"
    echo "LongLexTo sample/sample$i.txt cutword$i.csv"
done