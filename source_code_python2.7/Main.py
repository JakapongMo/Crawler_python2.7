import sys
import os

file_path = '/home/tengmo/crawler_to_server/store/4000filter.arc'
sub_path = '/home/tengmo/crawler_to_server/store/sub.arc'


def Use(line_1, line_2, line_3, line_4, line_5, line_6, html_content):
    print line_1
    print line_2
    print line_3
    print line_4
    print line_5
    print line_6
    #print html_content

######################################-MAIN-VARIABLE-##################################


#############################-Rotate-###################################################
cnt_rotate = 0
check_rotate = 1
iterator_rotate = 0
content = ""
line_1 = ''
line_2 = ''
line_3 = ''
line_4 = ''
line_5 = ''
line_6 = ''
html_content = ''
f = open(file_path, "r")
lineList = f.readlines()
index_rotate = -10;
for line in lineList:
    iterator_rotate +=1
    index_rotate += 1
    if len(line) > 7:
        if str(line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]) == 'http://':
            cnt_rotate += 1
            index_rotate = 1
    if index_rotate == 1:
        line_1 = line
    if index_rotate == 2:
        line_2 = line
    if index_rotate == 3:
        line_3 = line
    if index_rotate == 4:
        line_4 = line
    if index_rotate == 5:
        line_5 = line
    if index_rotate == 6:
        line_6 = line
    if index_rotate > 7:
        html_content += line
    if (cnt_rotate - check_rotate == 1) or (iterator_rotate == len(lineList)):
        check_rotate += 1
###############################-MAIN-RotateFuntion-######################################
        Use(line_1, line_2, line_3, line_4, line_5, line_6, html_content)

#########################################################################################
