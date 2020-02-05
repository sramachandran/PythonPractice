#fname = input("Enter file name: ")
#fh = open(fname,'r')
#ly=""
#count=0
#lz=0.0
#la=0
#lb=0
#for line in fh:
 #   if not line.startswith("X-DSPAM-Confidence:"):continue
  #  ly=line.rstrip()
   # la=int(ly.find(" ")+1)
    #lb=int(len(ly))
    #lz=lz+float(ly[la:lb])
    #count=count+1
#print("Average spam confidence:",lz/count)

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From "):continue
    ly=line.strip()
    ly=ly.split(' ')
    #lc=ly.split("From ",3)
    print(ly[1])
    count=count+1