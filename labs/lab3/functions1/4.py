def prime(a):
  if a == 1:
    return False
  for i in range(2, a):
   if a % i == 0:
     return False
  return True


a=list(map( int , input().split()))

for x in a :
  if prime(x): print(x , end=" ")

