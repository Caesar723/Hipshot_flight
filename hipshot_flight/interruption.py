import numpy as np
import random
from rotate import *


class Interruotion:# rect


    CONNECT=((1,2),(3,4),(5,6),(7,8),
            (1,3),(2,4),(5,7),(6,8),
            (1,5),(2,6),(3,7),(4,8))

   
    def __init__(self,x,y,z,level) -> None:
        seed=hash(f"{x}{y}{z}")
        random.seed(seed)
        self.difficult=level(seed)
        self.__matrix=np.matrix([
            [0,100,-100,100,-100,100,-100,100,-100],
            [0,100,100,100,100,-100,-100,-100,-100],
            [0,100,100,-100,-100,100,100,-100,-100]
        ])
        self.__matrix=change_Size(self.difficult.size)*self.__matrix
        self.__matrix[0]+=x
        self.__matrix[1]+=y
        self.__matrix[2]+=z

        self.angles=[0,0,0]
        
    
    def move(self):
        Rotate_Structure(self,*self.difficult.rotate)

    @property
    def Matrix(self):
        return self.__matrix
    
    @Matrix.setter
    def Matrix(self,matrix):
        self.__matrix=matrix
