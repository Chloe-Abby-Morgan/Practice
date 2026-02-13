class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}
        rList = []

        for i in strs:
            if ("".join(sorted(list(i)))) not in anaDict:
                anaDict["".join(sorted(list(i)))] = [i]
            else:
                anaDict["".join(sorted(list(i)))].append(i)
        
        for i in anaDict.values():
            rList.append(i)
        
        return rList

if __name__ == "__main__":
    lst = ["act","pots","tops","cat","stop","hat"]
    print(Solution().groupAnagrams(lst))