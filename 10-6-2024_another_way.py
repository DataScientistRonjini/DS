# Move all the zeroes at the end
# 2 pointer aprroach
n=[1, 2, 0, 4, 3, 0, 5, 0]
i=0
j=len(n)-1
while i<j:
    if n[i]!=0:
        i+=1
    else:
        n[i],n[j]=n[j],n[i]
        j-=1
print(n)