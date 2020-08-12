class MinStack(object):
    count = 0
    def getCount(self):
        return self.count
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.count +=1
        if not self.stack:
            self.stack.append((value,value))
        else:
            self.stack.append((value,min(value,self.stack[-1][1])))
    def pop(self):
        self.count -=1
        self.stack.pop()[0]
    def top(self):
        return self.stack[-1][0]
    def getMin(self):
        return self.stack[-1][1]
if __name__ == '__main__':
    test = MinStack()
    test.push("a")
    print(test.getCount())
    test.push("b")
    print(test.getCount())
    test.push("c")
    print(test.getCount())
    print("test")
    print(test.getMin())
    print(test.pop())
    print(test.getCount())
    print(test.top())
    print(test.getCount())
    print(test.getMin())
    print(test.getCount())
    print(test.pop())
    print(test.getCount())

