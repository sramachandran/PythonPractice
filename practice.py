sentance='this is my first interview'
sen=sentance.split()
sen_len=len(sen)
print(sen_len)
average=sum(len(word) for word in sen)/sen_len
print(average)