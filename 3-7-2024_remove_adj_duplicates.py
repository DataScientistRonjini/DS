# Remove adjacent duplicates
s="abbaca"
stack=[]

for c in s:
    if c in stack:
        stack.pop()
    else:
        stack.append(c)
print(stack,"stack")
    