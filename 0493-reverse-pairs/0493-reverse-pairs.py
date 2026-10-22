class Solution:
    def reversePairs(self, nums):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, count1 = merge_sort(arr[:mid])
            right, count2 = merge_sort(arr[mid:])
            count = count1 + count2
            j = 0

            for x in left:
                while j < len(right) and x > 2 * right[j]:
                    j += 1
                count += j

            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            return merged + left[i:] + right[j:], count

        return merge_sort(nums)[1]