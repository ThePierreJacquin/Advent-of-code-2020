
n_tree=0
pos=0

for line in open('day3.txt','r'):
    line=line.rstrip("\n")
    if line[ pos % (len(line)) ]=='#':
        n_tree+=1
    pos+=3

#########################################################

total=1

for inc in [1,3,5,7,0.5]:
    pos=0
    n_tree=0
    for line in open('day3.txt','r'):
        line=line.rstrip("\n")
        if (pos%1==0) & (line[ int(pos) % (len(line)) ]=='#'):
            n_tree+=1
        pos+=inc
    total*=n_tree


print(total)