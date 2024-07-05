# Next greatest temperature
# Example temperature: [30, 40, 50, 60]
# return array [1,1,1,0]
# Example 2 temperatures: [73, 74, 75, 71, 69, 72, 76, 73]
# return array [1, 1, 4, 2, 1, 1, 0, 0]

temperatures=[73, 74, 75, 71, 69, 72, 76, 73]

# Optimised
result=[0]*len(temperatures)
stack=[]

for index, value in enumerate(temperatures):
    while stack and temperatures[stack[-1]]<value:
        temp=stack.pop()
        result[temp]=index-temp
    stack.append(index)
print(result)