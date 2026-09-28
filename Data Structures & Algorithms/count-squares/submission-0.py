class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        key = (point[0], point[1])
        if key not in self.points:
            self.points[key] = 1
        else:
            self.points[key] += 1
    def count(self, point: List[int]) -> int:
        count = 0
        for p in self.points:
            if point[0] != p[0] and point[1] != p[1] and abs(point[0] - p[0]) == abs(point[1] - p[1]):
                if (p[0], point[1]) in self.points and (point[0], p[1]) in self.points:
                    count += self.points[(p[0], p[1])] * self.points[(p[0], point[1])] * self.points[(point[0], p[1])]
        return count
