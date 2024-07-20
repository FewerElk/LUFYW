#L.U.F.Y.W - Let Us Find Your Way

class LUFYW(object):
    def __init__(self):
        ...
        
    def calculate(self, points:tuple, ways:tuple, type:str):
        ...
        
class Point(object):
    def __init__(self, id:int, ways:tuple):
        self.ID = id
        self.WAYS = ways
        ...
        
class Way(object):
    def __init__(self, id:int, p1:Point, p2:Point):
        self.ID = id
        self.P1 = p1
        self.P2 = p2
        