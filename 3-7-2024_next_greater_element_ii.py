# Next Greater Element II
# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]

# nums = [1,2,3,4,3]
nums=[1,2,1]
stack=[nums[0]]

for n in range(len(nums)): 
    if nums[n] > stack[-1]:
        # stack.pop()
        stack.append(nums[n])
    elif nums[n] < stack[-1]:
        stack.append(-1)
stack.pop(0)
if nums[len(nums)-1]>max(stack):
    stack.append(-1)
else:
    stack.append(max(stack))

            
print(stack,"stack")
