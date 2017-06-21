'''
Created on 05/05/2013

@author: Pedro
'''
import pygame

def main():
    pygame.init()
    pantalla=pygame.display.set_mode([400,400])
    pygame.display.set_caption("Hanoi Rocks!")
    background_color=(120,49,24)
    asta_color=(120,134,67)
    cuadro_color=(0,0,255)
    objeto1=pygame.Surface((30,700))
    objeto1.fill(asta_color)
    cuadro1=pygame.Surface((200,70))
    cuadro1.fill(cuadro_color)
    r1=pygame.Rect(50,50,45,45)
    r2=pygame.Rect(130,50,45,45)
    
    #Insertamos reloj
    reloj1=pygame.time.Clock()
    
    #Definimos las variables
    salir=False
    
    while not salir:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if r1.colliderect(r2):
                    r2.height=0
                    r2.width=0
        reloj1.tick(20)        
        pantalla.fill(background_color)
        
        (r1.left,r1.top)=pygame.mouse.get_pos()
        r1.left-=r1.width/2
        r1.top-=r1.height/2
        
        pygame.draw.rect(pantalla,cuadro_color,r1)
        pygame.draw.rect(pantalla,asta_color,r2)
        pygame.display.update()
        
main()