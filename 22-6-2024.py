# Find K-Length Substrings With No Repeated Characters
# Input: S = "havefunonleetcode", K = 5
# Output: 6
# Explanation: 
# There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
s = "havefunonleetcode"
k = 5
res = 0
i = 0
curr = set()

for j in range(len(s)):
    while s[j] in curr:
        curr.remove(s[i])
        i += 1
    
    curr.add(s[j])

    if j - i + 1 == k:
        res += 1
        curr.remove(s[i])
        i += 1
    

print(res)
