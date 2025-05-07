class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def reset(self):
        self.x = 0
        self.y = 0

class Line(Point):
    def __init__(self, point_1:Point, point_2:Point):
        self.point_1 = point_1
        self.point_2 = point_2
        if((point_1.x-point_2.x)==0):
            self.slope = None
            self.cut_point = None
        elif((point_1.y-point_2.y)==0):
            self.slope = 0
            self.cut_point = point_1.y
        else:
            self.slope = (point_1.y-point_2.y)/(point_1.x-point_2.x)
            self.cut_point = -(point_1.y/self.slope)+point_1.x
    
    def correspondence(self, x:float, reverse:bool)->float:
        if(reverse==False):
            return (self.slope*x)+self.cut_point if(self.slope!=None) else self.point_1.x
        else:
            if(self.cut_point==None or self.slope==0):
                return None
            return (x-self.cut_point)/self.slope

class Rectangle:
    def __init__(self, width:float, height:float, bottom_left:Point):
        self.width = width
        self.height = height
        self.b_left = bottom_left
        self.t_right = Point(self.b_left.x+width, self.b_left.y+height)
        self.center = Point(self.b_left.x+(width/2), self.b_left.y+(height/2))

    def compute_area(self)-> float:
        return self.width*self.height

    def compute_perimeter(self)-> float:
        return (self.width*2)+(self.height*2)
    
    def compute_interference_point(self,point:Point)->bool:
        val_x:bool = point.x>=self.b_left.x and point.x<=self.b_left.x+self.width
        val_y:bool = point.y>=self.b_left.y and point.y<=self.b_left.y+self.height
        return val_y and val_x
    
    def compute_interference_line(self,line:Line)->bool:
        a:bool = self.b_left.y<=line.correspondence(self.b_left.x,0)<=self.t_right.y
        c:bool = self.b_left.y<=line.correspondence(self.t_right.x,0)<=self.t_right.y
        if(line.correspondence(self.t_right.y,1)!=None):
            b:bool = self.b_left.x<=line.correspondence(self.b_left.y,1)<=self.t_right.x
            d:bool = self.b_left.x<=line.correspondence(self.t_right.y,1)<=self.t_right.x
            return a or b or c or d
        return a or c

class Square(Rectangle):
    def __init__(self, side:float, bottom_left:Point):
        super().__init__(side, side, bottom_left)

punto1 = Point(3, 4)
punto2 = Point(6, 5)
rec = Rectangle(4 , 5, punto1)

punto3 = Point(6, 6)
cuadrado = Square(5, punto1)
linea = Line(punto2, punto3)

print(rec.center.x, cuadrado.height)
print(rec.compute_interference_point(punto2))
print(rec.compute_interference_line(linea))