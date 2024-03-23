def indexwiseSum(a,add):
    k=[]
    j=0
    for i in range(len(a)):    
        if(i==len(a)-1):
            k.append(a[i])
            if(sum(k)==add):
                print(k)
        else:
            if(sum(k)>add):
                k.remove(k[j])
                k.append(a[i])
            elif(sum(k)<add):
                k.append(a[i])
            else:
                print(k)
                k.append(a[i])

        
array=[2,8,9,3,6,5,4,1]
add=20
print(indexwiseSum(array,add))

# output:-
#if add=19
# [2, 8, 9]          
# [3, 6, 5, 4, 1] 
#if sum =20  
#None


