f= open('First.txt','a')
f.write("hello")
f.close()

f=open('First.txt','r')
print(f.read())