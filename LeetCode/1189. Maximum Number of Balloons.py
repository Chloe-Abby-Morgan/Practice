class Solution(object):
    def maxNumberOfBalloons(self, text):
        freq = {i : 0 for i in "balloon"}
        for i in text:
            freq[i] = freq.get(i,0) + 1
        return min(freq["a"],freq["b"],freq["n"],freq["l"]//2,freq["o"]//2)