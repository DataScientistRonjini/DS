# Remove adjacent duplicates

s="abbaca"
stack=[]
for st in s:
    if st not in stack:
        stack.append(st)
    elif st==stack[-1]:
        stack.pop()
print("".join(stack))