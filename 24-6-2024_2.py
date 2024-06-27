# Search a 2D Matrix
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
m=len(matrix)
n=len(matrix[0])-1
i=0
j=n
while i<m and j>0:
    if matrix[i][j]==target:
        print(True)
        break
        
    if matrix[i][j]>target:
        j-=1
    else:
        i+=1
if i==m or j==0:
    print(False)
    
        

    