import sys
import os
#"crawl-20170101054747-00000.arc.gz"
#command= os.popen("gunzip /home/tengmo/crawler_to_server/store/"+ sys.argv[1])
#datainput = command.read()

#command= os.popen("gunzip /home/tengmo/crawler_to_server/store/"+ sys.argv[1])
#datainput = command.read(iconv -f utf-8 -t utf-8 -c /home/tengmo/crawler_to_server/store/"+ sys.argv[1] >> /home/tengmo/crawler_to_server/store/"+"filter"+sys.argv[1])

name_file = sys.argv[1][0:len(sys.argv[1])-3]

#print name_file

command= os.popen("python /home/tengmo/crawler_to_server/source_code_python2.7/Find_site2.py name_file")
datainput = command.read()

command= os.popen("python /home/tengmo/crawler_to_server/source_code_python2.7/write_json2.py name_file")
datainput = command.read()

print finit
