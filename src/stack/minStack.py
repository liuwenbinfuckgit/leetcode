class MinStack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        if not self.stack:
            self.stack.append((value,value))
        else:
            self.stack.append((value,min(value,self.stack[-1][1])))
    def pop(self):
        self.stack.pop()[0]
    def top(self):
        return self.stack[-1][0]
    def getMin(self):
        return self.stack[-1][1]
if __name__ == '__main__':
    test = MinStack()
    test.push(-2)
    test.push(0)
    test.push(-3)
    print(test.getMin())
    print(test.pop())
    print(test.top())
    print(test.getMin())