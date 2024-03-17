def Majority(frequency,maximum):
    for key,value in frequency.items():
        if(value==maximum):
            print(key)
            break
List = [8,3,4,8,8]
frequency = {}

for i in List:
   if i in frequency:
      frequency[i] += 1
   else:
      frequency[i] = 1

print(frequency)
maximum=max(frequency.values())
print(Majority(frequency,maximum))



