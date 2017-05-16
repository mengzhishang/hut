#_*_coding:utf-8_*_

import re
fp = open('d:/TXL.txt','r')
# print (fp)
new_file = open('d:/666.vcf','w',encoding='utf-8')

while(True):
    line = fp.readline()
    find_name = re.compile(r'\w+')
    name = find_name.search(line)
    name = name.group()

    find_num = re.compile(r'\d+')
    num = find_num.search(line)
    num = num.group()
    if line:
        print (line)
        new_file.write("BEGIN:VCARD\nVERSION:3.0\n")
        new_file.write("N:;%s;;;\n"%name)
        new_file.write("FN:%s\n"%name)
        new_file.write("TEL;TYPE=CELL:%d\n"%int(num))
        new_file.write("END:VCARD\n")
        new_file.write('\n')
    else:
        break
