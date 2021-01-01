def heightChecker(a) -> int:
    count = 0
    c = [h1!=h2 for h1,h2 in zip(a,sorted(a))]
    for i in c :
        if i:
            count+=1
    return count



heights = [1,1,4,2,1,3]
lenght= heightChecker(heights)

print(lenght)
"""
Output: 3
Explanation:
Current array : [1,1,4,2,1,3]
Target array  : [1,1,1,2,3,4]
On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.

"""
