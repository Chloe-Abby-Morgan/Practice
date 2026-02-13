class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        sList = []

        for elt in nums:
            if elt not in frequency:
                frequency[elt] = 1
            else:
                frequency[elt] += 1
        
        for i in frequency.items():
            sList.append((i))
    
        sList = (sorted(sList, key = lambda x:x[1], reverse=True))[:k]
        return [sList[i][0] for i in range(len(sList))]
    
if __name__ == "__main__":
    lst, k = [1,2,2,3,3,3], 2
    print(Solution().topKFrequent(lst,k))