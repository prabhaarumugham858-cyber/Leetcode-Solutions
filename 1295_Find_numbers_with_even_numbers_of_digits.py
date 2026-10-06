class Solution:
    def findNumbers(self,num):
        count=0
        for num in nums:
            if len(str(num))%2==0:
                count=count+1
        return count