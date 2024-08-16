# Next Greater Element II
# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]

nums=[1,2,3,4,3]
n=len(nums)
res=[-1]*n
stack=[]

for i in range(2*n):
    num=nums[i%n]
    while stack and nums[stack[-1]]<num:
        res[stack.pop()]=num
    if i<n:
        stack.append(i)
print(res)
