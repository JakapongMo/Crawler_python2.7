import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
from bs4 import BeautifulSoup

file_path = '/home/tengmo/crawler_to_server/store/4000filter.arc'
HAVE_TITLE = 0
NO_TITLE = 0

############################################################################################
def Use(line_1, line_2, line_3, line_4, line_5, line_6, html_content):
    print line_1
    #print line_2
    print line_3
    #print line_4
    #print line_5
    #print line_6
    print html_content

############################################################################################

def Find_title_def(html_content):
    global HAVE_TITLE
    global NO_TITLE
    soup = BeautifulSoup(html_content, 'lxml', from_encoding="utf-8")

    #return soup.title

    try:
        if (soup.title.string) == None:
            NO_TITLE += 1
            return "No_title"

        else:
            HAVE_TITLE += 1
            return (soup.title.string)
    except AttributeError:
        NO_TITLE +=1
        return ("No_title")

############################################################################################

####################################-Rotate-###############################################
cnt_begin = 0
cnt_end = 1
iterator = 0
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
            #print line
    if (cnt_begin - cnt_end == 1) or (iterator == len(lineList)):
        cnt_end +=1

#######################################-Rotate-##############################################
        #Use(line_1, line_2, line_3, line_4, line_5, line_6, html_content)
        title =  Find_title_def(html_content)
        print line_1.rstrip()
        print title


############################################################################################
        line_1 = ''
        line_2 = ''
        line_3 = ''
        line_4 = ''
        line_5 = ''
        line_6 = ''
        html_content = ''

    if cnt_begin == cnt_end:
        if index == 1:
            line_1 = line
        if index == 2:
            line_2 = line
        if index == 3:
            line_3 = line
        if index == 4:
            line_4 = line
        if index == 5:
            line_5 = line
        if index == 6:
            line_6 = line
        if index == 7:
            html_content = ''
        if index > 7 :
            html_content += line
############################################################################################

print "No title :",NO_TITLE
print "Have title :",HAVE_TITLE
