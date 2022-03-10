class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        def peakindex(l, r):
            if nums[l] < nums[r]:
                return r
            while l <= r:
                mid = l + ((r - l) >> 1)
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    if nums[mid] < nums[l]:
                        r = mid - 1
                    else:
                        l = mid + 1

        def findindex(l, r):
            while l <= r:
                mid = l + ((r - l) >> 1)
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        size = len(nums)
        pindex = peakindex(0, size - 1)
        # print(nums[pindex])

        if target == nums[pindex]:
            return pindex
        elif target >= nums[0] and target <= nums[pindex]:
            return findindex(0, pindex)
        elif pindex + 1 < size and target >= nums[pindex + 1] and target <= nums[size - 1]:
            return findindex(pindex + 1, size - 1)
        else:
            return -1
