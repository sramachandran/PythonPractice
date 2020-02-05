fname=input('enter the name of the file:')
fh=open(fname,'r')
for line in fh:
    line=line.rstrip()
    print(line)
    wds=line.split()
    print(line)
    for w in wds:
        counts[w]=get(counts(w,0))+1