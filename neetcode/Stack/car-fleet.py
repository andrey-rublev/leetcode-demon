class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(speed)):
            time.append((target-position[i])/speed[i])
        sortPos, sortTime = zip(*sorted(zip(position, time)))
        time = list(sortTime)
        for i in range(len(time)-2, -1,-1):
            if time[i+1]>time[i]:
                time[i] = time[i+1]
        return len(Counter(time))