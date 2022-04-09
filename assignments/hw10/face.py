from graphics import Circle,Line

class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self,window,center,size):
        size=self.size
        center= self.center
        eye_size= 0.15 *size
        eye_off= size/3.0
        mouth_size=0.8 * size
        mouth_off= size/2.0

        self.head=Circle(center,size)
        self.head.draw(window)
        self.left_eye=Circle(center,eye_size)
        self.left_eye.move(-eye_off,-eye_off)
        self.right_eye=Circle(center,eye_size)
        self.right_eye.move(eye_off,-eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)

        point_1=center.clone()
        point_1.move(-mouth_size/2, mouth_off)
        point_2=center.clone()
        point_2.move(mouth_size/2,mouth_off)
        x1,x2=point_1.getX(),point_2.getX()
        midX=(x2-x1)/2+x1
        midY= point_1.getY()+ 20
        point_3=Point(midX,midY)
        self.mouth=Polygon(point_1,point_2,point_3)
        self.mouth.draw(window)

    def shock(self,window,center,size):
        self.mouth.undraw()
        eye_size= 0.15 * size
        eye_off= size/3.0
        mouth_size= 0.8 * size
        mouth_off= size/2.0

        self.head= Circle(center,size)
        self.head.draw(window)
        self.left_eye=Circle(center,eye_size)
        self.left_eye.move(-eye_off,eye_size)
        self.right_eye=Circle(center,eye_size)
        self.right_eye.move(eye_off,-eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)

        point_1= center.clone()
        point_1.move(0,mouth_off)
        self.mouth=Circle(point_1,eye_size)
        self.mouth.draw(window)
    def wink(self,window, center, size):
        self.left_eye.undraw()
        self.mouth.undraw()
        eye_size= 0.15 * size
        eye_off= size/ 3.0
        mouth_size=0.8 * size
        mouth_off= size/2.0
        self.head= Cirlce(center,size)
        self.head.draw(window)
        self.right_eye=Circle(center, eye_size)
        self.right_eye.move(eye_off,-eye_off)
        self.right_eye.draw(window)

        point_1=center.clone()
        point_1.move(-mouth_size/2, mouth_off)
        point_2= center.clone()
        point_2.move(mouth_size/2, mouth_off)
        x1,x2= point_1.getX(), point_2.getX()
        midX=(x2-x`)/2 +x1
        midY-point_1.getY() +50
        point_3= Point(midX,midY)
        self.mouth= Polygon(point_1,point_2,point_3)
        self.mouth.draw(window)

        leftPt= self.right_eye.getCenter()
        leftPt.move(-mouth_size,0)
        rightPt= leftPt.clone()
        rightPt.move(eye_size * 2,0)
        self.left_eye=Line(leftPt,rightPt)
        self.left_eye.draw(window)
