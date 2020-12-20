f=open("day8.txt",'r')

lines=f.read().split('\n')
test=[0] * len(lines)

acc=0
n=0

while test[n]==0:
    test[n]=1
    line=lines[n].split()
    
    if line[0]=='acc':
        acc+= int(line[1])
        n+=1
    
    if line[0]=='jmp':    
        n+=int(line[1])
    
    if line[0]=='nop':
        n+=1

print(acc)