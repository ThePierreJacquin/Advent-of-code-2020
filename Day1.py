liste = []
with open("day1.txt") as f:
    liste = list(map(int, f.readlines()))

for a in liste:
    for b in liste:
        if a+b==2020:
            print(a*b)

for a in liste:
    for b in liste:
        for c in liste:
            if a+b+c==2020:
                print(a*b*c)
