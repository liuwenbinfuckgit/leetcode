class Solution(object):
    result = []
    i=0
    def inorderTraversal(self, root):
        top = root[self.i]
        if len(root) == self.i:
            return
        if root[self.i+1] is not None:
            self.result.append(root[self.i+1])
            self.i+=1
            self.inorderTraversal(root)
        else:
            self.result.append(root[self.i])
            self.i+=2
            self.inorderTraversal(root)
if __name__ == '__main__':
    test = Solution()
    root = [1, None, 2, 3]
    test.inorderTraversal(root)
    print(test.result)
