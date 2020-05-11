def positive(n):
  result=0
  for i in range(1,n-1):
    result=result+(i*3)
  return result

print(positive(10))