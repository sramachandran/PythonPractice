from collections import Counter

cnt=Counter('civic')

d=dict(cnt)

for k, v in d.items():
    if v==1:
        print(True)
