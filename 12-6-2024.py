# 1. Given an array [1,2,3,4,1,5] create 2 boolean string represent whether 
# the element present in right or left side for this given input output will be [000010,100000]
n=[1,2,3,4,1,5]
left_set=set()
left_str=""
right_set=set()
right_str=""

for i in range(len(n)):
    if n[i] in left_set:
        left_str+="1"
    else:
        left_str+="0"
        left_set.add(n[i])

for i in range(-1,-(len(n)+1),1):
    if n[i] in right_set:
        right_str+="1"
    else:
        right_str+="0"
        right_set.add(n[i])
print(left_str,"left_str")
print(right_str,"right_str")

# output is coming to be
# 000010
# 000001
