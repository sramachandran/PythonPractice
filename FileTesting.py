x="X-DSPAM-Confidence: 0.6178"
y=int(x.find(" ")+1)
print(y)
z=int(len(x))
print(z)
print(x[y:z])