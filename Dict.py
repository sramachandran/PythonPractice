name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    if not line.startswith("From "): continue
    ly=line.split(" ")
    ly=ly[1]
    counts[ly]=counts.get(ly,0)+1
bigword=None
bigcount=None
for k,v in counts.items():
    if bigcount is None or v>bigcount:
        bigword=k
        bigcount=v
print(bigword,bigcount)