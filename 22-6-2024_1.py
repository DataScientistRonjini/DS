# Reurn the number of subtring in s of length k with no repeated characters
s="havefunonleetcode"
k=5
result=0
i=0
curr=set()

for j in range(len(s)):
    while s[j] in curr:
        print(curr,"before remove curr")
        curr.remove(s[j])
        print(curr,"curr")
        i+=1
        
    curr.add(s[j])
    print(i, j)
    if j-i+1>=k:
        result+=j-i+1
print(result)