# Check if string one is subsequence of other or n ot
# Input: str1 = “AXY”, str2 = “ADXCPY”
# Output: True (str1 is a subsequence of str2)

str1="AXY"
str2="ADXCPY"
i=0
j=0
while i<len(str1) and j<len(str2):
    if str1[i]==str2[j]:
        i+=1
        j+=1
    else:
        j+=1
if i==len(str1):
    print("str1 is subsequence of str2")
else:
    print("str1 is NOT a subsequence of str2")