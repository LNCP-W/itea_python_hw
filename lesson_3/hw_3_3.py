f1=open('file_1.txt', 'w')
f1.write('One - 1\nTwo - 2\nThree - 3\nFour - 4')
f1.close()

dictionary={'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
f1=open('file_1.txt','r')
f2=open('file_2.txt','w')
flag=1
while flag:
    line_f = f1.readline()
    if line_f != '':
        word_old=line_f.split()[0]
        line_f=line_f.replace(word_old, dictionary[word_old])
        f2.write(line_f)
    else: flag=0
f1.close()
f2.close()


