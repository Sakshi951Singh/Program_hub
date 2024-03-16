l=[-5,1,-2,3,-1,+2,-2]
current=0
max=0
for i in range(len(l)):
    if(current+l[i]<0):
        current=0
    else:
        current=current+l[i]
        if(current>max):
            max=current
print(max)
