class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        min_point = min(start, destination)
        max_point = max(start, destination)

        total_d = sum(distance)
        sum_m = sum(distance[min_point:max_point])
        return min(total_d - sum_m, sum_m)