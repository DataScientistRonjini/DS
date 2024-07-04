class Stack:
    def __init__(self):
        self.stack = []
        self.count = 0
        self.index = -1
    
    def push(self, ele):
        if self.index + 1 >= len(self.stack):
            # If the stack is full, resize it by doubling its capacity
            new_size = len(self.stack) * 2 if self.stack else 1
            new_stack = [None] * new_size
            for i in range(len(self.stack)):
                new_stack[i] = self.stack[i]
            self.stack = new_stack
        
        self.index += 1
        self.stack[self.index] = ele
        self.count += 1
    
    def pop(self):
        if self.count == 0:
            print("Stack is empty")
        else:
            self.stack[self.index] = None  # Optional: clear the slot
            self.index -= 1
            self.count -= 1

    def __str__(self):
        return str(self.stack[:self.index + 1])

# Example usage:
stk = Stack()
stk.push(2)
print(stk, "STACK")  # Output should be [2] STACK

stk.push(5)
print(stk, "STACK")  # Output should be [2, 5] STACK

stk.pop()
print(stk, "STACK")  # Output should be [2] STACK

stk.pop()
print(stk, "STACK")  # Output should be [] STACK

stk.pop()  # Output should be "Stack is empty"
