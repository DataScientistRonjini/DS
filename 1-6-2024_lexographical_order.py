# Remove the duplicate letter string every letter appears only once
# Lexiographical order maintain

s="cbacdcbc"
last_index={ value: key for key, value in enumerate(s)}
#print(last_index,"last_index")
check=set()
stack=[]

for index, ch in enumerate(s):
    if ch not in check:
        while stack and ch < stack[-1] and index<last_index[stack[-1]]:
            check.remove(stack.pop())
        check.add(ch)
        stack.append(ch)
print(stack)