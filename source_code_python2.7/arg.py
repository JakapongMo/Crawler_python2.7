#!/usr/bin/python

import sys

file_path = '/home/tengmo/crawler_to_server/store/4000filter.arc'

iterator = 0
cnt_begin =0
cnt_end =0
f = open(file_path, "r")
lineList = f.readlines()
index = -10;
line_1 = ''
line_2 = ''
line_3 = ''
line_4 = ''
line_5 = ''
line_6 = ''
html_content = ''
for line in lineList:
    iterator += 1
    #print line
    index += 1
    if len(line) > 7:
        if str(line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]) == 'http://':
            cnt_begin += 1
            index = 1
            print line
print iterator
