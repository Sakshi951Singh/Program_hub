def equilibrium(a):
    for i in range(len(a)):
        k=[]
        sum1=0
        # append indexwise sum in a list k.
        for i in range(len(a)): 
            sum1=sum1+a[i]
            k.append(sum1)
        # iterate in k[] and check condition to find the eqilibrium point
        for j in range(len(k)):
            if(k[len(k)-1]-k[j]==k[j-1]):
                index=j
    print("Equilibrium point is : ",a[index])

list=[3,4,8,-9,20,3,3]
equilibrium(list)

# output:
# Equilibrium point is :  20