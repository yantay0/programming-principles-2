lst=list(map (int , input().split()))

for  i in range (0 , len(lst)-1) :
   if lst[len(lst)-1]==1 : ok =1
   elif lst[i]==1: 
    lst[i+1] == lst[len(lst)-1]
    ok=1
   else : ok=0

print(ok)
#doesn't work

