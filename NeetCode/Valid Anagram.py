class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))
    
if __name__ == "__main__":
    s, t = "racecar", "carrace"
    print(Solution().isAnagram(s,t))