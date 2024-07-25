# Leetcode problem no 493


from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        return self.merge_sort(nums, 0, len(nums) - 1)
    
    def merge_sort(self, nums: List[int], left: int, right: int) -> int:
        if left >= right:
            return 0
        
        mid = (left + right) // 2
        count = 0
        count += self.merge_sort(nums, left, mid)
        count += self.merge_sort(nums, mid + 1, right)
        
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            count += j - (mid + 1)
        
        self.merge(nums, left, mid, right)
        
        return count
    
    def merge(self, nums: List[int], left: int, mid: int, right: int) -> None:
        temp = []
        i, j = left, mid + 1
        
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        
        while i <= mid:
            temp.append(nums[i])
            i += 1
        
        while j <= right:
            temp.append(nums[j])
            j += 1
        
        for i in range(left, right + 1):
            nums[i] = temp[i - left]

# Example usage
sol = Solution()
nums = [1, 3, 2, 3, 1]
print(sol.reversePairs(nums))  # Output: 2
