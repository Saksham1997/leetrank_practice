def numJewelsInStones(J,S):
    jewel_lis = list(J)
    stone_lis = list(S)
    c = 0
    for i in stone_lis:
        for j in jewel_lis:
            if i==j:
                c+=1
    return c


str1=input("Enter the Jewel string")
str2=input("Enter the stones string")
print(numJewelsInStones(str1,str2))
