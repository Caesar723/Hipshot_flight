#区块
import random
import pygame
from interruption import Interruotion
from rotate import *




def displayStructure(screen,struct,camera,color=(255,255,255)):
    matrix=cameraChange(struct.Matrix,camera)
    
    for conn in struct.CONNECT:
        pygame.draw.line(screen,color,(matrix[0,conn[0]],matrix[1,conn[0]]),
        (matrix[0,conn[1]],matrix[1,conn[1]]),1)



class Block:
    

    STAR='*'
    def __init__(self,No_x,No_y,level,interrupt_bool) -> None:
        get_random=lambda : int(random.random()*10)
        self.position=(No_x,No_y)
        random.seed(hash(f"{No_y}{No_x}"))
        self.stars=[]
        self.interrupt=0

        for star in range(get_random()//5):
            self.stars.append((get_random()*10+No_x*100,get_random()*10+No_y*100))

        if interrupt_bool:
            if level.APPEAR>random.random():
                self.interrupt=Interruotion(get_random()*10+No_x*100,get_random()*10+No_y*100,0,level)
        else:
            random.random()

            


    def display(self,font:pygame.font.Font,screen:pygame.Surface,offset,camera):
        self.display_stars(font,screen,offset)
        self.display_interrupt(screen,camera)

    def display_interrupt(self,screen:pygame.Surface,camera):
        if self.interrupt:
            if camera.flight.velocity_res<self.interrupt.difficult.speed:
                displayStructure(screen,self.interrupt,camera,(250,30,30))
            else:
                displayStructure(screen,self.interrupt,camera)
            self.interrupt.move()

    def display_stars(self,font:pygame.font.Font,screen:pygame.Surface,offset):
        for star in self.stars:
            screen.blit(font.render(self.STAR, True, (251,251,251)),(star[0]-offset[0,0],star[1]-offset[1,0]))

    def __repr__(self) -> str:
        return f"x_{self.position[0]},y_{self.position[1]}"
