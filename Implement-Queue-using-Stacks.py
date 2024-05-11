class MyQueue:

    def __init__(self):
        self.f_stack = []
        self.s_stack = []
        

    def push(self, x: int) -> None:
        self.f_stack.append(x)
        

    def pop(self) -> int:
        if self.s_stack:
            return self.s_stack.pop()

        while self.f_stack:
            self.s_stack.append(self.f_stack.pop()) 

        return self.s_stack.pop()  

    def peek(self) -> int:
        if self.s_stack:
            return self.s_stack[-1]
        return self.f_stack[0]
             
        
        

    def empty(self) -> bool:
        if self.f_stack == [] and self.s_stack == []:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
