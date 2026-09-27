class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        # 1. Build the prefix sum array
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        # 2. Zero-Copy Divide and Conquer via index pointers
        def merge_sort(left, right):
            # Base Case: Single element, no valid pairs to form
            if left >= right:
                return 0
                
            mid = (left + right) // 2
            
            # Recursively sort and count the left and right halves
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)
            
            # 3. Two-Pointer Sliding Window across the sorted boundary
            start = mid + 1
            end = mid + 1
            
            for i in range(left, mid + 1):
                # Advance 'start' until the difference hits the 'lower' bound
                while start <= right and prefix[start] - prefix[i] < lower:
                    start += 1
                # Advance 'end' until the difference exceeds the 'upper' bound
                while end <= right and prefix[end] - prefix[i] <= upper:
                    end += 1
                    
                # The valid range of sums is exactly the distance between pointers
                count += (end - start)
                
            # 4. C-Optimized In-Place Merge
            # Because left->mid and mid+1->right are already sorted, Python's Timsort 
            # handles this concatenation in exactly O(N) time at the C-execution level.
            prefix[left:right + 1] = sorted(prefix[left:right + 1])
            
            return count
            
        return merge_sort(0, len(prefix) - 1)