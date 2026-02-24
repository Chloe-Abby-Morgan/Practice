class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = []
        for char in s:
            if char.isalnum():
                cleanS.append(char.lower())
        cleanS = "".join(cleanS)
        
        left = 0
        right = len(cleanS) - 1

        while left < right:
            if cleanS[left] == cleanS[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
    
if __name__ == "__main__":
    print(Solution().isPalindrome("Was it a car or a cat I saw?"))