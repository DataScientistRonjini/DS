# Valid parenthesis
# s: It contains only characters
# An input string s is valid if:
# 1) Open bracket must be closed by  the same type of bracket
# 2) Open bracket must be closed in the correct order
# 3) Every closed bracket has corresponding open bracket of same type
# s:'()' return True
# s:'(]' return False
# s:'()[]{}' valid
# s="(]"
s="()["
dic={'(':')','[':']','{':'}'}
stack=[]

for i in s:
    if i in dic:
        stack.append(i)
    else:
        if len(stack)==0:
            print(False)
            break
        else:
            if dic[stack[-1]]==i:
                stack.pop()
            else:
                print(False)
                break
if len(stack)==0:
    print(True)
else:
    print(False)
        
