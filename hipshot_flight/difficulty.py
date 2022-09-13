import random

class Level:#difficult region:D<C<B<A<S<SS<CHINA

    SPEED_RANGE:tuple=(0,0)
    SIZE_RANGE:tuple=(0,0)
    UPGRADE:float=0.0
    APPEAR:float=0.0
    POWER:int=0
    def __init__(self,seed) -> None:
        random.seed(seed)
        rotate_angle=lambda speed,rm,ro1,ro2:((speed**2)/(rm**2+ro1**2+ro2**2+0.01))**0.5
        self.speed=random.randint(*self.SPEED_RANGE)
        if self.UPGRADE>random.random():
            self.speed*=2
        x,y,z=random.randint(-6,11),random.randint(-6,11),random.randint(-6,11)
        rotate_unit=rotate_angle(self.speed,x,y,z)
        self.rotate=(x*rotate_unit,y*rotate_unit,z*rotate_unit)
        self.size=random.uniform(*self.SIZE_RANGE)

class D(Level):

    SPEED_RANGE=(3,15)
    SIZE_RANGE=(0.1,0.3)
    UPGRADE=0.1
    APPEAR=0.02
    Name="D"
    POWER=1

class C(Level):

    SPEED_RANGE=(7,25)
    SIZE_RANGE=(0.2,0.4)
    UPGRADE=0.2
    APPEAR=0.1
    Name="C"
    POWER=2

class B(Level):
    SPEED_RANGE=(2,35)
    SIZE_RANGE=(0.1,0.5)
    UPGRADE=0.4
    APPEAR=0.15
    Name="B"
    POWER=4


class A(Level):
    SPEED_RANGE=(35,75)
    SIZE_RANGE=(0.07,0.3)
    UPGRADE=0.3
    APPEAR=0.2
    Name="A"
    POWER=5

class S(Level):
    SPEED_RANGE=(100,135)
    SIZE_RANGE=(0.1,0.7)
    UPGRADE=0.1
    APPEAR=0.50
    Name="S"
    POWER=8


class SS(Level):
    SPEED_RANGE=(200,435)
    SIZE_RANGE=(0.02,0.3)
    UPGRADE=0.3
    APPEAR=0.55
    Name="SS"
    POWER=4
    POWER=10

class CHINA(Level):
    SPEED_RANGE=(2000,4000)
    SIZE_RANGE=(0.1,1)
    UPGRADE=0
    APPEAR=0.95
    Name="CHINA"
    POWER=20

if __name__=="__main__":
    print(D(22).rotate)