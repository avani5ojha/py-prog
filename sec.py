sum=0
a=[]
while True:


   choice=input("do u want to continue y for yes")
   if choice=='y':
        a.append(int(input()))
   else:
       break        

for i in a:
    sum=sum+i

print(sum)
