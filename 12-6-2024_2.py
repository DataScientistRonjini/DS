# Sort array by parity
# The task is to move all even numbers to the front (beginning) of the array 
# and place all odd numbers towards the rear (end) of the array.
nums = [3, 8, 5, 13, 6, 12, 4, 1]
i=0
j=len(nums)-1

while i<j:
    if nums[i]%2==0:
        nums[i],nums[j]=nums[j],nums[i]
        j-=1
    else:
        i+=1
print(nums)