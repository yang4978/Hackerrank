import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x;
        self.y = y;
        self.z = z;

    def __sub__(self, point):
        result = Points(0,0,0)
        result.x = self.x-point.x
        result.y = self.y-point.y
        result.z = self.z-point.z
        return result

    def dot(self, point):
        return (self.x*point.x+self.y*point.y+self.z*point.z);

    def cross(self, point):
        result = Points(0,0,0)
        result.x = self.y*point.z-self.z*point.y
        result.y = self.z*point.x-self.x*point.z
        result.z = self.x*point.y-self.y*point.x
        return result
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
