class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow = fast = i

            while True:
                nxt = next_index(slow)
                if nums[nxt] == 0 or (nums[nxt] > 0) != direction:
                    break
                slow = nxt

                for _ in range(2):
                    nxt = next_index(fast)
                    if nums[nxt] == 0 or (nums[nxt] > 0) != direction:
                        fast = -1
                        break
                    fast = nxt

                if fast == -1:
                    break

                if slow == fast:
                    if next_index(slow) != slow:
                        return True
                    break

            slow = i
            while nums[slow] != 0 and (nums[slow] > 0) == direction:
                nxt = next_index(slow)
                nums[slow] = 0
                slow = nxt

        return False