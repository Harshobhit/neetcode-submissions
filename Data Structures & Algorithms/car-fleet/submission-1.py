class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_time_to_target = []

        for p, s in sorted(zip(position, speed), reverse=True):
            time_to_target = (target - p) / s
            if fleet_time_to_target and time_to_target <= fleet_time_to_target[-1]:
                continue
            else:
                fleet_time_to_target.append(time_to_target)
        
        return len(fleet_time_to_target)