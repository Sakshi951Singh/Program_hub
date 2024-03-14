l4=[11,7,10,4,3,6,5,2]
print(len(l4))
max=0
for i in range(len(l4)-1,-1,-1):
    if(l4[i]>max):
        max = l4[i]
        print(max,end=" ")