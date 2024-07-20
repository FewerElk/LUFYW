#L.U.F.Y.W - Let Us Find Your Way

class LUFYW(object):
    def __init__(self):
        ...
        
    def calculate(self, points:tuple, ways:tuple, p1:Point, p2:Point):
        self.browsed = [p1,]
        if True:
            try:
                return self._rec(p1, p2)
            except:
                return (False,)
            
    def _rec(self, base, stop):
        for pt in base.connectedto:
            if pt in self.browsed:
                continue
            self.browsed.append(base)
            if stop.ID == pt.ID:
                return [True, base, stop]
            else:
                rep = self._rec(pt, stop)
                if rep[0]:
                    return rep.append(base)
                
                
        
class Point(object):
    def __init__(self, id:int, conto:tuple):
        self.ID = id
        self.connectedto = conto
        ...
        
class Way(object):
    def __init__(self, id:int, p1:Point, p2:Point, dist:int):
        self.ID = id
        self.P1 = p1
        self.P2 = p2
        self.distance = dist
        