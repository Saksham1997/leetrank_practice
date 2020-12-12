lis=[3,4,2]
num1=0
for i in range(len(lis)):
    num1=lis[i]*(10**i)+num1 #add the number at positon i from list and add it to 10^i to the newnumber that is being created
    #print(num1)

print("outside loop value is %d" % num1)
