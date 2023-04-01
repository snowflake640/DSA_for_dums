class Solution:
    def containsDuplicate(self, nums):
        flag = 0
        new_nums = set()
        for i in nums:
            if i in new_nums:
                return print(True)
            new_nums.add(i)

        if flag == 0: return print(False)

test = Solution()
test.containsDuplicate([1,2,3,4])