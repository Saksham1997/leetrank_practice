def decompressRLElist(nums):
    lis=[]
    i=0
    while i in range(len(nums)-1):
        freq=nums[i]
        val=nums[i+1]
        i+=2
        print("freq and val is {} {}".format(freq,val))
        for j in range(freq):
            lis.append(val)
            print("list now is {}".format(lis))
    return lis


print(decompressRLElist([1,2,3,4]))
