import pygame

def main():
    #Invocamos las funciones de Pygame
    pygame.init()
    
    #Modificamos aspectos de ventana
    pantalla=pygame.display.set_mode([1000,550])
    pygame.display.set_caption("Hanoi Rocks!")
    background_color=(120,49,24)
    asta_color=(120,134,67)
    cuadro_color1=(0,0,255)
    cuadro_color2=(3,0,25)
    cuadro_color3=(0,57,5)
    cuadro_color4=(46,0,56)
    cuadro_color5=(0,26,255)
    cuadro_color6=(45,0,65)
    cuadro_color7=(30,46,255)
    cuadro_color8=(57,49,5)
    cuadro_color9=(0,0,45)
    cuadro_color10=(0,0,76)
    cuadro_color11=(210,34,52)
    cuadro_color12=(45,80,100)
    cuadro_color13=(0,43,201)
    cuadro_color14=(34,23,86)
    cuadro_color15=(56,231,43)
    cuadro_color16=(23,56,2)
    r1=pygame.Rect(127,135,55,25)
    r2=pygame.Rect(122,161,70,25)
    r3=pygame.Rect(115,187,85,25)
    r4=pygame.Rect(108,213,100,25)
    r5=pygame.Rect(100,239,115,25)
    r6=pygame.Rect(94,265,130,25)
    r7=pygame.Rect(88,291,145,25)
    r8=pygame.Rect(82,317,160,25)
    r9=pygame.Rect(74,343,175,25)
    r10=pygame.Rect(66,369,190,25)
    r11=pygame.Rect(59,395,205,25)
    r12=pygame.Rect(50,421,220,25)
    r13=pygame.Rect(43,447,235,25)
    r14=pygame.Rect(34,473,250,25)
    r15=pygame.Rect(27,500,265,25)
    r16=pygame.Rect(20,526,280,25)
    asta1=pygame.Rect(140,103,30,450)
    asta2=pygame.Rect(450,103,30,450)
    asta3=pygame.Rect(800,103,30,450)
    
    #Insertamos reloj
    reloj1=pygame.time.Clock()
    
    #Definimos las variables
    salir=False
    
    while not salir:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if r1.colliderect([r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16]):
                    r1.width=0
                    r1.height=0
                        
                        
        reloj1.tick(20)        
        pantalla.fill(background_color)
        pygame.draw.rect(pantalla,asta_color,asta1)
        pygame.draw.rect(pantalla,asta_color,asta2)
        pygame.draw.rect(pantalla,asta_color,asta3)
        pygame.draw.rect(pantalla,cuadro_color1,r1)
        pygame.draw.rect(pantalla,cuadro_color2,r2)
        pygame.draw.rect(pantalla,cuadro_color3,r3)
        pygame.draw.rect(pantalla,cuadro_color4,r4)
        pygame.draw.rect(pantalla,cuadro_color5,r5)
        pygame.draw.rect(pantalla,cuadro_color6,r6)
        pygame.draw.rect(pantalla,cuadro_color7,r7)
        pygame.draw.rect(pantalla,cuadro_color8,r8)
        pygame.draw.rect(pantalla,cuadro_color9,r9)
        pygame.draw.rect(pantalla,cuadro_color10,r10)
        pygame.draw.rect(pantalla,cuadro_color11,r11)
        pygame.draw.rect(pantalla,cuadro_color12,r12)
        pygame.draw.rect(pantalla,cuadro_color13,r13)
        pygame.draw.rect(pantalla,cuadro_color14,r14)
        pygame.draw.rect(pantalla,cuadro_color15,r15)
        pygame.draw.rect(pantalla,cuadro_color16,r16)
        pygame.display.update()
    
main()