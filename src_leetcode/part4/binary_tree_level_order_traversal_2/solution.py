class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if root:
            tmp = []
            floor = []
            count_next = 0
            count = 1
            tmp.append(root)
            while tmp:
                node = tmp.pop(0)
                if node:
                    if node.left:
                        tmp.append(node.left)
                        count_next += 1
                    if node.right:
                        tmp.append(node.right)
                        count_next += 1
                    floor.append(node.val)
                    if len(floor) == count:
                        ret.append(floor)
                        count = count_next
                        count_next = 0
                        floor = []
        ret.reverse()
        return ret