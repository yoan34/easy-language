
verbs = []
doublon = []
with open("verbs.txt", "r") as f:
    for line in f:
        line = line.replace('\n', '')
        a = line.split(';')
        print(f"HELLO: {a}")
        if a[0] not in verbs:
            verbs.append(a[0])
        else:
            doublon.append(a[0])

print(verbs)
print(len(verbs))
print(doublon)
print(len(doublon))
        