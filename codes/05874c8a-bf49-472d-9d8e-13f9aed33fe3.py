from collections import defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        numOfWord = len(words)
        wordLen = len(words[0])
        n = len(s)

        ans = []

        wordCounter = defaultdict(lambda: 0)
        for w in words:
            wordCounter[w] += 1
        
        for k in range(wordLen):
            i = k
            counter = defaultdict(lambda: 0)
            for j in range(k, n, wordLen):
                currStr = s[j:j+wordLen]

                if currStr not in wordCounter:
                    counter = defaultdict(lambda: 0)
                    i = j+wordLen
                else:
                    counter[currStr] += 1

                    while counter[currStr] > wordCounter[currStr]:
                        counter[s[i:i+wordLen]] -= 1 
                        i += wordLen

                    if j-i == wordLen * (numOfWord-1):
                        ans.append(i)
        return ans
# Example usage
s = input()
words = input().split()
solution = Solution()
print(solution.findSubstring(s, words))