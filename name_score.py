scores = [(1000,'hus')]

i = int(input('\tEnter you choice(1Add/2Query): '))

while i != 0:
    if i == 1:
        name = input("\tEnter Name: ")
        score = int(input("\tEnter score: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse = True)
        scores = scores[:6]
        i = int(input('\tEnter you choice(1Add/2Query)1/2): '))
    
    elif i == 2:
        print("\tName\tscore")
        for entry in scores:
            score, name = entry
            print("\t", name, "\t", score)
        i = int(input('\tEnter you choice(1Add/2Query): '))
    else:
        print("\tBye~!")
        break
