name = input('Enter file name: ')
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if not line.startswith("From "):continue
    ly=line.split(" ")
    time=ly[6]
    pieces=time.split(":")
    element=pieces[0]
    counts[element]=counts.get(element,0)+1

tmp=list()
for k in counts:
    v=counts[k]
    tmp.append((v,k))

tmp.sort()
for (v,k) in tmp:
    print(k, v)



