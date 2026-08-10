class MinStack:
#basically we have 3 stacks one that counts the elements that comes to the stack
# and the other MinStack that mainly counts the min vaules that has been added to stack

    def __init__(self):

        self.stack = []
        self.minStack = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
# for 2nd stack ie min stack -> we need to see if there is alrady a value inserted in the minstack
# then we take the min of the input val and the minStack top value / minimum value
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        

