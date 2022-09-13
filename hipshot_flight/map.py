
import random
import pygame
from block import Block
from difficulty import *




class Map:

    HIGH=800
    WIDE=800
    
    level={10000:CHINA,5000:SS,3000:S,2000:A,1000:B,200:C,0:D}

    def __init__(self) -> None:
        self.font=pygame.font.SysFont('Helvetica', 12)
        self.Difficult_font=pygame.font.SysFont('Helvetica', 25)
        self.blocks:dict[int:dict]={}
        self.interruptions_distoried=set()
        self.Current_Difficult="D"
        

    

    def set_camera(self,camera):
        self.camera=camera

    def find_difficulty(self,x,y):
        distance=(x**2+y**2)**0.5
        for length in self.level:
            if distance>=length:
                return self.level[length]

    
        
    def display_filght_velocity(self,screen,flight):
        screen.blit(self.font.render(str(round(flight.velocity_res,2)), True, (251,251,251)),(50,50))

    def difplay_difficult(self,screen):
        screen.blit(self.Difficult_font.render(self.Current_Difficult, True, (251,25,25)),(650,50))

    def display_background(self,screen:pygame.Surface,camera):
        get_offset=self.camera.offset
        for row in self.blocks:
            for col in self.blocks[row]:
                self.blocks[row][col].display(self.font,screen,get_offset,camera)

    def check_boundary(self):
        camera_matrix=self.camera.Matrix
        
        for row in range(camera_matrix[1,0]//100-6,camera_matrix[1,0]//100+6):
            if row not in self.blocks:
                
                self.blocks[row]={}
            for col in range(camera_matrix[0,0]//100-6,camera_matrix[0,0]//100+10):
                if col not in self.blocks[row]:
                    difficult=self.find_difficulty(col,row)
                    self.Current_Difficult=difficult.Name
                    if f"{row}{col}" in self.interruptions_distoried:
                        self.blocks[row][col]=Block(col,row,difficult,False)
                    else:
                        self.blocks[row][col]=Block(col,row,difficult,True)
        

        self.check_out(camera_matrix[1,0]//100-7,-1,
                        camera_matrix[1,0]//100+7,1,
                        camera_matrix[0,0]//100-7,-1,
                        camera_matrix[0,0]//100+11,1)
        

    def check_out(self,out_row_min,change_row_min:int,
                            out_row_max,change_row_max,
                            out_col_min,change_col_min,
                            out_col_max,change_col_max):
        for row in dict(self.blocks):
            if row*change_row_min > out_row_min*change_row_min or\
                row*change_row_max > out_row_max*change_row_max:
                del self.blocks[row]
            else:
                for col in dict(self.blocks[row]):
                    if col*change_col_min>out_col_min*change_col_min or \
                        col*change_col_max>out_col_max*change_col_max:
                        del self.blocks[row][col]
        

    def check_flight_collision(self,flight):
        flight_matrix=flight.Matrix
        
        x_block=int(flight_matrix[0,0]//100)
        y_block=int(flight_matrix[1,0]//100)
        
        for y in range(y_block-1,y_block+1):

            for x in range(x_block-1,x_block+1):
                
                if self.blocks[y][x].interrupt:
                    interrupt_matrix=self.blocks[y][x].interrupt.Matrix
                    if (self.blocks[y][x].interrupt.difficult.size*150)**2>\
                        (flight_matrix[0,1]-interrupt_matrix[0,0])**2+(flight_matrix[1,1]-interrupt_matrix[1,0])**2:
                        
                        
                        if flight.velocity_res>=self.blocks[y][x].interrupt.difficult.speed:
                            flight.MAX_VELOCITY+=1
                            flight.velocity_res+=1
                        else:
                            flight.MAX_VELOCITY-=1
                            flight.velocity_res-=1

                        if self.find_difficulty(x,y).Name!="CHINA":
                            self.interruptions_distoried.add(f"{y}{x}")
                        self.blocks[y][x].interrupt=0
                
if __name__=="__main__":
    Map()
