# Move all zeroes at the end
n=[1, 2, 0, 4, 3, 0, 5, 0]
arr=[]
count=0
for i in range(len(n)):
    if n[i]!=0:
        arr.append(n[i])
    else:
        count+=1

arr+=count*[0]
