#  The task is to move all even numbers to the front (beginning) of the array 
#  and place all odd numbers towards the rear (end) of the array.
n=[3, 8, 5, 13, 6, 12, 4, 1]
i=0
j=len(n)-1

while i<j:
    if n[i]%2==1:
        n[i],n[j]=n[j],n[i]
        j-=1
    else:
        i+=1
print(n)
