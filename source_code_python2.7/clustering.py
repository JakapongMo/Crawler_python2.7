#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from sklearn.cluster import KMeans
import numpy as np

#json_data=open('/home/tengmo/crawler_to_server/output/json_dict.json').read()

data= eval(open("/home/tengmo/crawler_to_server/output/json_dict.txt").read())
#print data['http://area-family.com/']

print data
print data['http://ads.thaiware.com/www/admin/password-recovery.php']['Array_Feature']

INPUT_URL = []
for URL in data:
    print data[URL]['Array_Feature']
    INPUT_URL.append(data[URL]['Array_Feature'])

print INPUT_URL
x = np.array(INPUT_URL)
kmeans = KMeans(n_clusters=3, random_state=0).fit(x)
print kmeans.cluster_centers_


for URL in data:
    print kmeans.predict(data[URL]['Array_Feature'])
