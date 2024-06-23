# Move zeroes at the end
# single pointer approach
n=[1, 2, 0, 4, 3, 0, 5, 0]
zero=0
for i in range(len(n)):
    if n[i]!= 0:
        n[zero],n[i]=n[i],n[zero]
        zero+=1
print(n)