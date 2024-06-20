# Move all zeroes to the end
n=[1, 2, 0, 4, 3, 0, 5, 0]
i=0
j=len(n)-1
while i < j:
    if n[i]==0:
        n.append(n[i])
        del n[i]
    i+=1
print(n)
        