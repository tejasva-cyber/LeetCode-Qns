class Solution(object):
    def preorder(self, root):
        if not root:
            return []
            
        # 1. Manual Execution Stack Allocation
        stack = [root]
        result = []
        
        while stack:
            # 2. Process the parent node immediately
            node = stack.pop()
            result.append(node.val)
            
            # 3. Push children in reverse to guarantee left-to-right execution
            if node.children:
                stack.extend(reversed(node.children))
                
        return result