# -*- coding: utf-8 -*-
import sys
import glob


file_path = '/home/tengmo/crawler_to_server/store/4000filter.arc'
output_path = '/home/tengmo/crawler_to_server/output/dict_site.txt'


def Find_site(line_1):
    URL = ''
    Nb_point =0
    Nb_slash =0

    cnt = 0
    for char in line_1:
        cnt +=1
        if char == ' ':
            break
        if char == '.':
            Nb_point +=1
        if char == '/':
            Nb_slash +=1
        if Nb_slash == 3:
            break
        if Nb_point == 2:
            break
        if cnt > 7:
            URL += char
    if "www." in URL:
        cnt = 0
        new_URL =''
        for char in URL:
            cnt+=1
            if cnt >4:
                new_URL += char
    else:
        new_URL =''
        for char in URL:
            if char == '.':
                break
            new_URL += char
    return new_URL

######################################-MAIN-VARIABLE-##################################
my_dict = {}

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
        site = Find_site(line_1)
        if site in my_dict:
            my_dict[site] += 1
        else:
            my_dict[site] = 1

#########################################################################################

print (str(my_dict))
with open(output_path , 'w') as out:
    out.write("{")
    for k,v in my_dict.items():
        out.write("\"")
        out.write(str(k))
        out.write("\"")
        out.write(":")
        out.write(str(v))
        out.write(",")
        out.write('\n')
    out.write("}")
