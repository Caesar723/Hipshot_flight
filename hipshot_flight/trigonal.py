import numpy as np
from rotate import *


SCREEN_SIZE=(800,800)



RESULTANT=lambda x,y:(x**2+y**2)**0.5





class Triangle:
    MAX_VELOCITY=10
    CONNECT=((1,2),(1,3),(1,4),
            (2,3),(2,4),(3,4))

    MOVE=False


    def __init__(self,x,y,z) -> None:
        len_Tri=50
        high=90
        center_line=lambda le:(le/2)*3**0.5

        self.__matrix=np.matrix([
            [0,       0,        0,             len_Tri/2,-len_Tri/2],
            [0,high*2/3,-high*1/3,             -high*1/3,-high*1/3],
            [0,       0,center_line(len_Tri)*2/3,-center_line(len_Tri)*1/3,-center_line(len_Tri)*1/3]
        ],np.int32)
        
        self.__matrix[0]+=x
        self.__matrix[1]+=y
        self.__matrix[2]+=z

        self.velocity_res=0
        self.velocity_x=0
        self.velocity_y=0

       

        self.angles=[270,270,270]#x y z

        self.lastMouseInfo=None
        

    def set_camera(self,camera):
        self.camera=camera

    @property
    def Matrix(self):
        return self.__matrix
    
    @Matrix.setter
    def Matrix(self,matrix):
        self.__matrix=matrix

    

    @property
    def position(self):
        pos=cameraChange(self.__matrix[:,0],self.camera)
        
        return (pos[0,0],pos[1,0])

    @position.setter
    def position(self,newPos):
        self.Matrix+=np.matrix([[newPos[0]],[newPos[1]],[0]])
        
    def event(self,mouse_pos):
        Rotate_Structure(self,np.cos(2*np.pi*self.angles[2]/360)*self.velocity_res,
        np.sin(2*np.pi*self.angles[2]/360)*self.velocity_res,0)
        
        if self.MOVE :
            if self.velocity_res<=self.MAX_VELOCITY:
                self.velocity_res*=1.01
                self.velocity_res+=0.01
            elif self.velocity_res<0:
                self.velocity_res=0
            else:
                self.velocity_res=self.MAX_VELOCITY
            self.move(mouse_pos)
            
        
        else:
            if self.velocity_res>0 :
                self.velocity_res/=1.1
                self.velocity_res-=0.01
            else:
                self.velocity_res=0
            self.move()
        

    def move(self,position=0):
        if position:
            mou_pos=position
            get_pos=self.position
        
            dx,dy=mou_pos[0]-get_pos[0],mou_pos[1]-get_pos[1]
            res=RESULTANT(dx,dy)
            direction=int(get_pos[1]-mou_pos[1])


            self.lastMouseInfo=(dx,dy,res,direction)
            
            
        elif self.lastMouseInfo:
            dx,dy,res,direction=self.lastMouseInfo
        else:
            return
        

        self.velocity_x=self.velocity_res* dx/res
        self.velocity_y=self.velocity_res* dy/res

        self.position=(self.velocity_x,self.velocity_y)
        
        if  direction<0:
            Rotate_Structure(self,0,0,self.angles[2]-(360-360*np.arccos(dx/res)/(2*np.pi)))
        else:
            Rotate_Structure(self,0,0,self.angles[2]-360*np.arccos(dx/res)/(2*np.pi))
        
        self.adjust_angle(direction)


    def adjust_angle(self,direction):
        
        d_angle=np.arctan((self.__matrix[1,1]-self.__matrix[1,0])/(self.__matrix[0,1]-self.__matrix[0,0]))-\
            np.arctan(self.lastMouseInfo[1]/self.lastMouseInfo[0])
        if abs(d_angle>0.001):
            get_angle=-360*d_angle/(2*np.pi)
            if abs(get_angle)<160:
                Rotate_Structure(self,0,0,get_angle,0)
                if (self.__matrix[1,0]-self.__matrix[1,1])*direction<0:
                    Rotate_Structure(self,0,0,180,0)

           

            
            
            
        
        
        







if __name__=="__main__":
    Triangle(400,400,0)
