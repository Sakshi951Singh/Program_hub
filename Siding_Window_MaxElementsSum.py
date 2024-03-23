def SlidingWindow(list,k):
    # if list is smaller than window size
    if(len(list)<=k):
        return list
    max=0
    #iterate the loop for len(list)-k+1 times to reduce the iteration time
    for i in range(len(list)-k+1):
        sum1=sum(list[i:i+k])
        print(sum1)
        if(max<sum1):
            max=sum1
    return max


list = [1,8,30,-5,20,7]
k=3
print("Maximumn sum : ",SlidingWindow(list,k))