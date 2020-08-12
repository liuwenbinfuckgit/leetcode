# 使用两个栈构建一个队列
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

class CQueue(object):
    def getCount(self):
        return self.minStack.getCount()
    def __init__(self):
        self.minStack = MinStack()
        self.tempMinStack = MinStack()

    def appendTail(self, value):
        self.minStack.push(value)
    def deleteHead(self):
        if self.tempMinStack.getCount()!=0:
            temp = self.tempMinStack.top()
            self.tempMinStack.pop()
            return temp
        count = self.minStack.getCount()
        if count == 0:
            return -1
        for i in range(count):
            value =self.minStack.top()
            self.minStack.pop()
            self.tempMinStack.push(value)
        temp =self.tempMinStack.top()
        self.tempMinStack.pop()
        return temp
if __name__ == '__main__':
    test = CQueue()

    print(test.deleteHead())
    test.appendTail("5")
    test.appendTail("2")
    print(test.deleteHead())
    # print(test.getCount())
    print(test.deleteHead())
    # print(test.getCount())
    # test.appendTail("c")
    # print(test.getCount())
    # print(test.deleteHead())
    # print(test.getCount())
    # print(test.deleteHead())


