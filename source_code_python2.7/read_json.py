#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json

#json_data=open('/home/tengmo/crawler_to_server/output/json_dict.json').read()

data= eval(open("/home/tengmo/crawler_to_server/output/json_dict.json").read())
#print data['http://area-family.com/']


#data = [s.encode('utf-8') for s in data]
#print data['http://area-family.com/']
