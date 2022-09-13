import numpy as np



OFFSET=(100,0)
class Camera:

    Min_diff_pos=(-50+OFFSET[0],-50+OFFSET[1])
    Max_diff_pos=(50+OFFSET[0],50+OFFSET[1])


    def __init__(self) -> None:
        self.__matrix=np.matrix([[400],[400],[-1600]])

    def set_flight(self,flight):
        self.flight=flight

    def check_flight_out(self):
        flight_matrix=self.flight.Matrix
        if flight_matrix[0,0]>self.Max_diff_pos[0]+self.__matrix[0,0]:
            self.__matrix[0,0]=flight_matrix[0,0]-self.Max_diff_pos[0]
        elif flight_matrix[0,0]<self.Min_diff_pos[0]+self.__matrix[0,0]:
            self.__matrix[0,0]=flight_matrix[0,0]-self.Min_diff_pos[0]

        if flight_matrix[1,0]>self.Max_diff_pos[1]+self.__matrix[1,0]:
            self.__matrix[1,0]=flight_matrix[1,0]-self.Max_diff_pos[1]
        elif flight_matrix[1,0]<self.Min_diff_pos[1]+self.__matrix[1,0]:
            self.__matrix[1,0]=flight_matrix[1,0]-self.Min_diff_pos[1]

    @property
    def Matrix(self):
        return self.__matrix
    
    @Matrix.setter
    def Matrix(self,position):
        self.__matrix+=np.matrix([[position[0]],[position[1]],[0]])

    @property
    def offset(self):
        return np.matrix([[self.__matrix[0,0]-400],[self.__matrix[1,0]-400],[0]])

if __name__=="__main__":
    ca=Camera()
    print(ca.offset)