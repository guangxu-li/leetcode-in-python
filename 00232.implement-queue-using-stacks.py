#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []


    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.load()
        return self.output.pop()

    def peek(self) -> int:
        self.load()
        return self.output[-1]

    def load(self) -> None:
        if self.output:
            return

        self.output = self.input[::-1]
        self.input = []


    def empty(self) -> bool:
        self.load()
        return not self.output



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
