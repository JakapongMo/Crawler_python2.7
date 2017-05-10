# -*- coding: utf-8 -*-
import sys
import os
import csv
import glob
import urllib.parse
from bs4 import BeautifulSoup


path = '/home/tengmo/workwithcrawler/2000file/*.arc'
#path = '/home/tengmo/workwithcrawler/store/*.arc'
files = glob.glob(path)

TH =0
ENG =0
OTHER = 0
NO_CONTENT =0
error = 0
####################-subdef-#######################
def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return True

            index += 1

    return False

####################-maindef-#####################
def Find_URL(f):
    URL = ''
    Nb_slash = 0
    before = ''
    for line in f:
        for char in line:
            if char == '/':
                Nb_slash +=1
            if char  == ' ':
                if before == '/':
                    Nb_slash -=1
                break
            URL += char
            before = char
        break

    URL = urllib.parse.unquote(URL)
    yield URL
    yield Nb_slash - 2
    yield len(URL)- 7 - Nb_slash +1

def Find_binary_domain(URL):
    Domain_name = ''
    for char in URL[7:]:
        if(char == '/'):
            break
        Domain_name += char
    #print(Domain_name)

    list_string = ['.com', '.edu', '.gov', '.org', '.net', '.mil', '.co.th', '.in.th', '.ac.th']
    list_domain = [0,0,0,0,0,0,0,0,0,0]
    for x in range(0,9):
        if(find_str(Domain_name, list_string[x])):
            list_domain[x] += 1
    count = 0
    for x in range(0,9):
        if(list_domain[x] == 0):
            count +=1
    if count == 9:
        list_domain[9] +=1

    #print("binary_vector")
    #for x in range(0,10):
    #    print(list_domain[x])

    return list_domain

#    com = 0
#    edu = 0
#    gov = 0
#    org = 0
#    net = 0
#    mil = 0
#    co_th = 0
#    in_th = 0
#    ac_th = 0
#    other = 0

def Find_Nb_link_pic_table(f):
    text = ''
    cnt = 0
    for line in f:
        cnt +=1
        if(cnt>7):
            text += line
    html_content = text

    soup = BeautifulSoup(html_content, 'lxml')
    soup.find_all('a')

    newtitle = ''
    title = str(soup.title)
    for x in range(0, len(title)):
        if (x>6 and x < len(title)-8):
            newtitle += title[x]
    #print(newtitle)
    list_link = (soup.find_all('a'))
    list_table = (soup.find_all('table'))
    list_picture = (soup.find_all('img'))
    #print ('Nb of link: ',len(list_link))
    #print('Nb of table',len(list_table))
    #print('Nb of picture',len(list_picture))

    yield newtitle
    yield len(list_link)
    yield len(list_table)
    yield len(list_picture)

#############wordcount######################
def Wordcount_Thai(text):
    global error
    count_word = 0
    stopword =  ["กล่าว","กว่า","กัน","กับ","การ","ก็","ก่อน","ขณะ","ขอ","ของ","ขึ้น","คง","ครั้ง","ความ",
            "คือ","จะ","จัด","จาก","จึง","ช่วง","ซึ่ง","ดัง","ด้วย","ด้าน","ตั้ง","ตั้งแต่","ตาม","ต่อ","ต่าง",
            "ต่างๆ","ต้อง","ถึง","ถูก","ถ้า","ทั้ง","ทั้งนี้","ทาง","ที่","ที่สุด","ทุก","ทํา","ทําให้","นอกจาก","นัก",
            "นั้น","นี้","น่า","นํา","บาง","ผล","ผ่าน","พบ","พร้อม","มา","มาก","มี","ยัง","รวม","ระหว่าง",
            "รับ","ราย","ร่วม","ลง","วัน","ว่า","สุด","ส่ง","ส่วน","สําหรับ","หนึ่ง","หรือ","หลัง","หลังจาก",
            "หลาย","หาก","อยาก","อยู่","อย่าง","ออก","อะไร","อาจ","อีก","เขา","เข้า","เคย","เฉพาะ","เช่น",
            "เดียว","เดียวกัน","เนื่องจาก","เปิด","เปิดเผย","เป็น","เป็นการ","เพราะ","เพื่อ","เมื่อ","เรา","เริ่ม",
            "เลย","เห็น","เอง","แต่","แบบ","แรก","และ","แล้ว","แห่ง","โดย","ใน","ให้","ได้","ไป","ไม่",
			"ไว้","ก","ข","ฃ","ค","ฅ","ฆ","ง","จ","ฉ","ช","ซ","ฌ","ญ","ฎ","ฏ","ฐ","ฑ","ฒ",
			"ณ","ด","ต","ถ","ท","ธ","น","บ","ป","ผ","ฝ","พ","ฟ","ภ","ล","ว","ศ",
            "ษ","ห","ฬ","อ","ฮ", "จาก", "ๆ", "นะ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

    with open('/home/tengmo/workwithcrawler/output_thai/cutword/input.txt' , 'w') as out:
        out.write(text)
    command= os.popen("cat input.txt")
    datainput = command.read()
    #print(datainput)
    command= os.popen("java LongLexTo input.txt output.csv")
    datainput = command.read()
    #print(datainput)
    with open('/home/tengmo/workwithcrawler/output_thai/cutword/output.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        try:
            for row in reader:
                if row['word'] not in stopword:
                    count_word += 1
                    #print(row['word'])
        except csv.Error:
            error += 1
            return 0
        #except UnicodeDecodeError:
        #    error += 1
        #    return 0
    return count_word

def Wordcount_Eng(text):
    stopword = ['all', "she'll", 'just', "don't", 'being', 'over', 'through',
    		   'yourselves', 'its', 'before', "he's", "when's", "we've", 'had',
    			'should', "he'd", 'to', 'only', "there's", 'those', 'under',
    			'ours', 'has', "haven't", 'do', 'them', 'his', "they'll", 'get',
    			'very', "who's", "they'd", 'cannot', "you've", 'they', 'not',
    			'during', 'yourself', 'him', 'nor', "we'll", 'like', 'did',
    			"they've", 'this', 'she', 'each', "won't", 'where', "mustn't",
    			"isn't", "i'll", "why's", 'www', 'because', "you'd", 'doing',
    			'some', 'up', 'are', 'further', 'ourselves', 'out', 'what',
    			'for', 'while', "wasn't", 'does', "shouldn't", 'above', 'between',
    			'ever', 'ought', 'be', 'we', 'who', "you're", 'were', 'here',
    			'hers', "aren't", 'by', 'both', 'about', 'would', 'of', 'could',
    			'against', "i'd", "weren't", "i'm", 'com', 'or', "can't", 'own',
    			'into', 'whom', 'down', "hadn't", "couldn't", "wouldn't", 'your',
    			"doesn't", 'from', "how's", 'her', 'their', "it's", 'there',
    			'been', 'why', 'few', 'too', 'themselves', 'was', 'until', 'more',
    			'himself', "where's", "i've", 'with', "didn't", "what's", 'but',
    			'else', 'herself', 'than', "here's", 'he', 'me', "they're",
    			'myself', 'these', "hasn't", 'below', 'r', 'can', 'theirs', 'my',
    			'k', "we'd", 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself',
    	     	'at', 'have', 'in', 'any', 'if', 'again', 'no', 'that', 'when',
    			'same', 'how', 'other', 'which', 'you', "shan't", 'http', 'shall',
    			'our', 'after', "let's", 'most', 'such', 'on', "he'll", 'a', 'off',
    			'i', "she'd", 'yours', "you'll", 'so', "we're", "she's", 'the',
    			"that's", 'having', 'once','.']

    wordcount = {}
    count= 0
    for word in text.split():
        if word.lower() not in stopword:
            count += 1
    return count

def Convert_to_Eng(text):
    new_text = ''
    for char in text:
        #try:
        if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >=97 and ord(char) <=122) or ord(char)==40 or ord(char) ==10 or ord(char)==32) or (ord(char) >= 45 and ord(char) <= 58):
            new_text += char
        #except (TypeError, ValueError):
        #    pass
    return new_text

def Convert_to_Thai(text):
    ans = ''
    for char in text:
        if(ord(char) >= 3584 and ord(char) <= 3711):
            ans += char
    new_text = "".join(ans.split())
    return new_text

def Wordcount(content, title, charset):
    if (charset == "Thai"):
        content = Convert_to_Thai(content)
        title = Convert_to_Thai(title)
        #print (title)

        count_title = Wordcount_Thai(title)
        count_content = Wordcount_Thai(content)
        count_content -= count_title
        global TH
        TH += 1
        yield count_title
        yield count_content

    elif (charset == "Eng"):
        content = Convert_to_Eng(content)
        title = Convert_to_Eng(title)
        count = Wordcount_Eng(content)
        count_title = Wordcount_Eng(title)
        count_content = count - count_title
        #print ("title :", title)
        global ENG
        global NO_CONTENT
        if count_title == 0 and count_content == 0:
            NO_CONTENT += 1
        else:
            ENG += 1
        yield count_title
        yield count_content

    elif (charset == "Other"):
        yield -1
        yield -1

def Find_content(name):
    html = html_content(name)
    content = get_content_total(html)
    return content

def check_charset(title):
    cnt = 0
    template = 'a'
    for x in title:
        template = x;
        break
    #print (template)
    char = template
    if(ord(char) >= 3584 and ord(char) <= 3711):
        return "Thai"
    if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >=97 and ord(char) <=122) or ord(char)==40 or ord(char) ==10 or ord(char)==32) or (ord(char) >= 45 and ord(char) <= 60):
        return "Eng"
    else:
        return "Other"

def html_content(name):
    f = open(name, 'r')
    text = ''
    cnt = 0
    for line in f:
        cnt +=1
        if(cnt>7):
            text += line
    html_content = text
    return html_content
def get_content_total(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    text = soup.get_text()
    return text
def get_title(html_content):
    f = open(name, 'r')
    text = ''
    cnt = 0
    for line in f:
        cnt +=1
        if(cnt>7):
            text += line
    html_content = text
    soup = BeautifulSoup(html_content, 'lxml')
    title = soup.title
    return title
############################################
#global OTHER
#global NO_CONTENT
cnt=0
for name in files:
    try:
        cnt += 1
        #if cnt ==3:
        #    break
        with open(name) as f:
            print(name ,' ',cnt)
            content = Find_content(name)
            title , link , table, picture = Find_Nb_link_pic_table(f)
            #print (title)
            #try:
            count_title, count = Wordcount(content, title, check_charset(title))
        #   except (TypeError, ValueError):
            #    pass
            #print (title)
            print ("count title : ", count_title)
            print ("count content: ", count)

            if (count == -1 and count_title == -1 ):
                OTHER +=1



            '''
                URL, Nb_slash, URL_length = Find_URL(f)
                print('URL : ',URL,'\n','Nb of slash : ',Nb_slash,'\n','URL_length : ',URL_length)
                Find_binary_domain(URL)
                list_domain = Find_binary_domain(URL)
                print("binary_vector")
                for x in range(0,10):
                    print(list_domain[x])
                title , link , table, picture = Find_Nb_link_pic_table(f)
                print ('Nb of link: ', link)
                print('Nb of table', table)
            print('Nb of picture',picture)
            '''

    except IOError as exc:
        if exc.errno != errno.EISDIR:
            print('Yo!!')
            error += 1
            raise
print ("error : " , error)
print ("other_language : " , OTHER)
print ("thai : " , TH)
print ("Eng : " , ENG)
print ("NO_CONTENT : " , NO_CONTENT)
