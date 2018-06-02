a=[]
sum=0
n=0




def fun(n):
    global sum
    a.append(n)
    print(a)
    choice=raw_input("do you want to enter more. no for no")
    if choice=="no":
        print("jello")
    #     """for i in a:
    #         sum=sum+ i
    #     print(sum)
    else:
        fun(int(choice))







fun(0)
