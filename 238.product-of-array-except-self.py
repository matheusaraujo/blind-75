#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # prefix, postfix, result = [1] * n, [1] * n, [1] * n

        # prefix[0] = 1
        # for i in range(1, n):
        #     prefix[i] = prefix[i - 1] * nums[i - 1]

        # postfix[n - 1] = 1
        # for i in range(n - 2, -1, -1):
        #     postfix[i] = postfix[i + 1] * nums[i + 1]

        # for i in range(n):
        #     result[i] = prefix[i] * postfix[i]

        # return result
        n = len(nums)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1] # prefix

        postfix = 1

        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


# @lc code=end

