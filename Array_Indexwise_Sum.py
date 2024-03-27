def Array_indexwiseSum(a,start,end):
    k=[]
    sum1=0
    # append indexwise sum in a list k.
    for i in range(len(a)): 
        sum1=sum1+a[i]
        k.append(sum1)
    print(k)
    
    if start==0:
        print(k[end])
    else:
        print("sum = ",k[end]-k[start-1])      
        

list=[2,8,3,9,6,5,4]
start=int(input("Enter the starting ponit : "))
end=int(input("Enter the ending ponit : "))
Array_indexwiseSum(list,start,end)

# Output:-
# Enter the starting ponit : 1
# Enter the ending ponit : 6
# [2, 10, 13, 22, 28, 33, 37]
# sum = 35

