f=open('day4.txt','r')
passeports=f.read().split("\n\n")
infos={'byr','iyr','eyr','hgt','hcl','ecl','pid'}

n_valide=0
for passeport in passeports:
    valide=1
    for info in infos:
        if info not in passeport:
            valide=0
    n_valide+=valide


print(n_valide)