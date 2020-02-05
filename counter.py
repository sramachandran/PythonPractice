from collections import Counter
cnt = Counter()
for word in ['red','blue']:
    cnt[word] += 1
print(cnt)