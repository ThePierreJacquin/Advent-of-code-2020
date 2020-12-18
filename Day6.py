f=open("day6.txt","r")

n_total=0
for groupe in f.read().split('\n\n'):
    y_groupe=set()

    for answers in groupe:
        y_groupe.add(answers)
    
    if '\n' in groupe:
        y_groupe.remove('\n')
    n_total+=len(y_groupe)
f.close()

###############################################

f=open("day6.txt","r")

n_total=0
for groupe in f.read().split('\n\n'):
    
    personnes=groupe.split('\n')
    
    answers=set(personnes[0])
    
    for i in range (len(personnes)):
        answers=answers&set(personnes[i])

    n_total+=len(answers)

print(n_total)