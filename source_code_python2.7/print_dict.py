import sys
import os


dict_site = eval(open("/home/tengmo/crawler_to_server/output/dict_site.txt").read())
#dict_site = eval(open("/home/tengmo/workwithcrawler/new_source_code/dict_site.txt").read())

for k,v in dict_site.items():
    print (k, " : ",v)
