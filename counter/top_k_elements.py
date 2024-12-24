# top k frequent elements
from collections import Counter, List

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    cnt = Counter(nums)
    return [num for num, freq in cnt.most_common(k)]

nums = [1,1,1,2,2,3]
print(topKFrequent(nums))