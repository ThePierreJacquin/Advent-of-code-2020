from typing import Counter


f=open("day2.txt","r")
line=f.readline()

valid=0

while line:
    split1=line.split('-')
    min=int(split1[0])
    
    split2=split1[1].split(' ')
    
    max=int(split2[0])
    letter=split2[1][0]
    
    pswd=split2[2]
    if pswd.count(letter)<=max and pswd.count(letter)>=min:
        valid+=1
    line=f.readline()
f.close()

print(valid)


###################


f=open("day2.txt","r")
line=f.readline()

valid=0

while line:
    split1=line.split('-')
    pos1=int(split1[0])
    
    split2=split1[1].split(' ')
    
    pos2=int(split2[0])
    letter=split2[1][0]
    
    pswd=split2[2]
    if (pswd[pos1-1]==letter) ^ (pswd[pos2-1]==letter):
        valid+=1
    line=f.readline()
f.close()

print(valid)