class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        if not schedule or len(schedule) == 0:
            return [[]]
        time = []
        for employee in schedule:
            for slot in employee:
                time.append(slot)

        time.sort(key=lambda x: x.start)

        ans = []
        max_end = time[0].end

        for i in range(1, len(time)):
            if max_end < time[i].start:
                ans.append(Interval(max_end, time[i].start))
            max_end = max(max_end, time[i].end)

        return ans
