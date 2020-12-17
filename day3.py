f=open('day3.txt','r')

line=f.readline()

treenbr=0
pos=0
line=f.readline()

while line:  
    pos+=3
    if pos>=len(line):
        pos=pos-len(line)
    
    if line[pos]=='#':
        treenbr+=1
    line=f.readline()

print(treenbr)