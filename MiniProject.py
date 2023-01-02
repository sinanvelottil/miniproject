a=int(input("Enter the first no of the range: "))
b=int(input("Enter the second no of the range: "))
prime_list=[]
composite_list=[]
if a<0 or b<0:
    print("Entered range includes negative numbers")
else:
    for i in range(a,b+1):
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            prime_list.append(i)
    for i in range(a,b+1):
        if i not in prime_list:
            composite_list.append(i)
    p=list(set(prime_list))
    c=list(set(composite_list))
    total_list=p+c
    total_list.sort()
    for i in total_list:
        if i in prime_list:
            print(i,"is prime")
        else:
            print(i,"is composite")
    print("Count:",len(p),"prime and",len(c),"composite numbers in the range.")
    