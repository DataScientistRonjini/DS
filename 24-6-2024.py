# Count Pairs Whose Sum is Less than Target
nums=[-1,1,2,3,1]
target=2
count=0
i=0
j=len(nums)-1
while i<j:
    if nums[i]+nums[j]<target:
        count+=j-i
        i+=1
        print(i,j)
    else:
        j-=1
print(count)
