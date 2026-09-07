import collections

class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
            
        queue = collections.deque([root])
        result = []
        
        # Standard Breadth-First Search (BFS)
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # Append the current level's values
            result.append(current_level)
            
        # Reverse the final array to get bottom-up order
        return result[::-1]