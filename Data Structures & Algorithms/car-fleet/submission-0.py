class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_time_to_target = {}

        for p, s in zip(position, speed):
            time_to_target = (target - p) / s
            if fleet_time_to_target.get(time_to_target):
                fleet_time_to_target[time_to_target].append(p)
            else:
                fleet_time_to_target[time_to_target] = [p]
        
        return len(fleet_time_to_target)