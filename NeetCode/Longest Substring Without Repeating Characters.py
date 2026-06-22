class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        length = 0

        while right < len(s):
            if s[right] not in s[left:right]:
                right += 1
                length = max(length, (right-left))
            else:
                left += 1
        return length