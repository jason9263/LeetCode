class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        if not slots1 or not slots2:
            return []

        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        i, j = 0, 0

        while i < len(slots1) and j < len(slots2):
            cur_start = max(slots1[i][0], slots2[j][0])
            cur_end = min(slots1[i][1], slots2[j][1])
            if cur_end - cur_start >= duration:
                return [cur_start, cur_start + duration]
            if slots1[i][1] < slots2[j][1]:
                i = i + 1
            else:
                j += 1

        return []
