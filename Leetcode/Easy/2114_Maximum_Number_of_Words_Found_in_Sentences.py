class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        largest=0
        for i in sentences:
            words=i. split()
            count=len(words)
            if count>largest:
                largest=count
        return largest