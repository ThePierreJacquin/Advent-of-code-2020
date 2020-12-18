max_id=0
list_id=[]
for line in open("day5.txt","r"):
    
    maxrow=127
    minrow=0
    for x in line[:7]:
        if x=='F':
            maxrow=(minrow+maxrow-1)/2
        else:
            minrow=(1+minrow+maxrow)/2
    assert minrow==maxrow

    maxcol=7
    mincol=0
    for x in line[7:-1]:
        if x=='L':
            maxcol=(mincol+maxcol-1)/2
        else:
            mincol=(mincol+maxcol+1)/2
    assert mincol==maxcol

    list_id.append(8*minrow+mincol)
    max_id=max(max_id,8*minrow+mincol)

print(max_id)

for id in range (1,int(max_id-1)):
    if (id not in list_id) and (id-1 in list_id) and (id+1 in list_id):
        print(id)  