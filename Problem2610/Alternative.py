class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        num_count = {}
        maximum = 0
        result = []
        # Count frequency of num in nums
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1
            maximum = max(maximum, num_count[num])
        # Create empty lists
        for i in range(maximum):
            result.append([])
        # Filling the lists
        for num, count in num_count.items():
            for i in range(count):
                result[i].append(num)
        return result