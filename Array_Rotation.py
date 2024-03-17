def right_rotation(l2,start,end):
    for i in range(end, start-1, -1):
        print(l2[i], end=" ")
    for j in range(len(l2)-1,end,-1):
        print(l2[j], end=" ")

def left_rotation(l2,start,end):
    for i in range(len(l2)-end-2, start-1, -1):
        print(l2[i], end=" ")
    for j in range(len(l2)-1,(len(l2)-end)-2,-1):
        print(l2[j], end=" ")


l1=[1,2,3,4,5]
l2=l1[::-1]
print(len(l2))
right=int(input("how many times you want to rotate: "))
print("After right rotation : ")
right_rotation(l2,0,right-1)
print()
print("After left rotation : ")
left_rotation(l2,0,right-1)




