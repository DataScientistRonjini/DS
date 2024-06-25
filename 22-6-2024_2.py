# Input: s = "abcd"
# Output: 10
# Explanation: Since each character occurs once, every substring is a special substring. We have 4 substrings of length one, 3 of length two, 2 of length three, and 1 substring of length four. So overall there are 4 + 3 + 2 + 1 = 10 special substrings.
# Example 2:

# Input: s = "ooo"
# Output: 3
# Explanation: Any substring with a length of at least two contains a repeating character. So we have to count the number of substrings of length one, which is 3.
from collections import defaultdict
s="abcd"
left=0
total=0
n=len(s)
dict=defaultdict(int)

for right in range(n):
    dict[s[right]]+=1
    while dict[s[right]]>1:
        dict[s[left]]-=1
        left+=1
    total+=right-left+1

print(total)
        