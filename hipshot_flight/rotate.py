import numpy as np



def cameraChange(struct,camera):
    
    return Rotate(0,5,0)*(struct-camera.Matrix)+camera.Matrix-camera.offset
    
def cameraRechange(struct,camera):
    
    return Rotate(0,-5,0)*(struct-camera.Matrix)+camera.Matrix-camera.offset

def angleConvert(angle):

    return np.pi*2*angle/360

def change_Size(size):
    return np.matrix([
        [size,0,0],
        [0,size,0],
        [0,0,size]
    ])

def Rz(angle):

    angle=angleConvert(angle)
    result=np.matrix([
        [np.cos(angle),-np.sin(angle),0],
        [np.sin(angle),np.cos(angle),0],
        [0,0,1]
    ])

    return result

def Ry(angle):

    angle=angleConvert(angle)
    result=np.matrix([
        [np.cos(angle),0,-np.sin(angle)],
        [0,1,0],
        [np.sin(angle),0,np.cos(angle)]
    ])

    return result

def Rx(angle):

    angle=angleConvert(angle)
    result=np.matrix([
        [1,0,0],
        [0,np.cos(angle),-np.sin(angle)],
        [0,np.sin(angle),np.cos(angle)]
    ])

    return result

def Rotate(x,y,z):
    return Ry(y)*Rx(x)*Rz(z)

def Rotate_Structure(struct,x,y,z,record=1):
    
    matrix=struct.Matrix
    difference=np.matrix(matrix[:,0])
    matrix-=difference
    
    struct.Matrix=(Rotate(x,y,z)*matrix)+difference
    
    

    if record:
        struct.angles[0]=(struct.angles[0]-x)%360
        struct.angles[1]=(struct.angles[1]-y)%360
        struct.angles[2]=(struct.angles[2]-z)%360
    


    

if __name__=="__main__":
    print(np.matrix([[1],[0],[0]]))
    print(Rz(90)*np.matrix([[1],[0],[0]]))