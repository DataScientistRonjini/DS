# Count Pairs Whose Sum is Less than Target
# nums = [-1,1,2,3,1], target = 2
nums = [-6,2,5,-2,-7,-1,3]
nums.sort()
target = -2
i=0
count=0
j=len(nums)-1
while i<j:
    if nums[i]+nums[j]<target:
        count+=j-i
        i+=1    
    else:
        j-=1
print(count)
        