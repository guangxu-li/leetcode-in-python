#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
class Node():
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None

    def insert(self, node):
        if node.start < self.end and node.end > self.start:
            return False

        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        else:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True 
        
        return self.root.insert(Node(start, end))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

