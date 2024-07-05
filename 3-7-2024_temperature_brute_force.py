# Next greatest temperature
# Example temperature: [30, 40, 50, 60]
# return array [1,1,1,0]
# Example 2 temperatures: [73, 74, 75, 71, 69, 72, 76, 73]
# return array [1, 1, 4, 2, 1, 1, 0, 0]

temperatures=[73, 74, 75, 71, 69, 72, 76, 73]

# Brute force
result=[]
i=0
j=0
for i in range(len(temperatures)-1):
    for j in range(i+1, len(temperatures)):
        if temperatures[j]>temperatures[i]:
            result.append(j-i)

print(result)