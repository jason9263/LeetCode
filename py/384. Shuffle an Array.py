import copy


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)
        # self.original = copy.deepcopy(nums)

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums) - 1, 0, -1):
            r = random.randint(0, i)
            self.nums[i], self.nums[r] = self.nums[r], self.nums[i]

        return self.nums
