class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        a_list=[]
        for i in range(len(arr)-2) :
            for j in range(i+1,len(arr)-1):
                for k in range(j+1,len(arr)):
                    if abs(arr[i] - arr[j])<=a:
                        if abs(arr[j]-arr[k])<=b:
                            if abs(arr[i]-arr[k])<=c:
                                t=tuple((arr[i],arr[j],arr[k]))
                                a_list.append(t)
        if not a_list:
            return 0
        return len(a_list)


ab=Solution()
lis=[3,0,1,1,9,7]
print(ab.countGoodTriplets(lis,7,2,3))
