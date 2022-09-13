from camera import Camera
from rotate import *
from trigonal import Triangle
from block import displayStructure
from map import Map
import pygame
import time







        

    
def initinal_object():
    triang=Triangle(400,400,0)
    camera=Camera()
    triang.set_camera(camera)
    camera.set_flight(triang)
    Ma=Map()
    Ma.set_camera(camera)
    return (triang,camera,Ma)
    

def main():
    pygame.init()
    pygame.display.set_caption('hipshot flight')
    
    screen=pygame.display.set_mode((800,800))

    triang,camera,Ma=initinal_object()

    frame=time.time()
    
    while 1:
        if time.time()-frame>0.01:
            frame=time.time()
            screen.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    triang.MOVE=True
                if event.type ==pygame.MOUSEBUTTONUP:
                    triang.MOVE=False
                    
            
            Ma.display_background(screen,camera)
            Ma.display_filght_velocity(screen,triang)
            Ma.difplay_difficult(screen)
            displayStructure(screen,triang,camera)
            triang.event(pygame.mouse.get_pos())
            camera.check_flight_out()
            Ma.check_boundary()
            Ma.check_flight_collision(triang)
            
            


        pygame.display.flip()
if __name__=="__main__":
    
    
    
    main()
