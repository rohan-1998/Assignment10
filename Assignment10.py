'''#Question 1
f=open("test.txt",'r')
lines=f.readlines()
n=int(input("enter the number"))
for i in range(n):
    print(lines[i],end="")
f.close()

f=open("test.txt",'r')
count=0
a=f.readline()
for i in range(len(a)):
    if(a[i]==" "):
        count+=1
print(count)


#Question 2
f=open('test.txt')
data=f.read()
c=data.split()
print(c)
for word in c:
    count=c.count(word)
    print(word,count)
f.close()


#Question 3
f=open("test.txt",'r')
a=f.read()
print(a)
f1=open("test2.txt",'w')
f1.write(a)
f.close()
f1.close()'''

#Question4
f1=open("file3.txt")
f2=open("file4.txt")
f3=open("file5.txt","w")
l=f1.readlines()
for i in l:
    a=f2.readline().strip('\n')
    f3.write(a+i)
       
f1.close()
f2.close()
f3.close()
'''
#Question 5
import random as r
f=open("file1.txt",'w')
for i in range(10):
    a=r.randint(1,9)
    f.write(str(a)+"\n")
f.close() 
f=open("file1.txt","r")
a=f.readlines()
f.close()
f=open("file2.txt",'w')
for i in range(len(a)):
    f.write(a[i])
f.close()
'''
