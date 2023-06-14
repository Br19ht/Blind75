class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for point in points:
            point.append((point[0] ** 2 + point[1] ** 2) ** 1/2)

        sortedPoints = sorted(points, key = lambda x: int(x[2]))
        print(sortedPoints)

        for i in range(k):
            res.append([sortedPoints[i][0], sortedPoints[i][1]])

        return res