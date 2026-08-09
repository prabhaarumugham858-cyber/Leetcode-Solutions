class Solution:
    def runningSum(self, nums):
        answer = []
        total = 0

        for i in nums:
            total = total + i
            answer.append(total)

        return answer