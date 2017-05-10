import os

command= os.popen("python3 Main.py")
data = command.read() 
with open('/home/tengmo/workwithcrawler/output_thai/cutword/doo.txt' , 'a') as out:
	out.write(data)
print (data)


'''
data = data.split(',')
for x in range(1, int(data[0])+1):
	print x
for x in range(1, int(data[1])+1):
	print x
for x in range(1, int(data[2])+1):
	print x
'''
