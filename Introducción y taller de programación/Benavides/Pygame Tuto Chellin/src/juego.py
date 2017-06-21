import pygame
import random
import pygame.mixer

def main():
    pygame.init()
    pygame.mixer.init(30000)
    pygame.mixer.music.load("thud.mp3")
    pantalla=pygame.display.set_mode([550,550])
    salir=False
    reloj1=pygame.time.Clock()
    fuente1=pygame.font.SysFont("Verdana", 15, True, True)
    info=fuente1.render("Ten seconds",0,(255,255,255))
    texto1=fuente1.render("HOLIS",0,(34,67,255))
    listarec=[]
    segundosint=0
    rotos=0
    termino=False
    r1=pygame.Rect(0,0,10,10)
    for x in range(15):
        w=random.randrange(10,50)
        h=random.randrange(10,50)
        x=random.randrange(500)
        y=random.randrange(500)
        listarec.append(pygame.Rect(x,y,w,h))
        
    while not salir:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                for recs in listarec:
                    if termino==False:
                        if r1.colliderect(recs):
                            pygame.mixer.music.play()
                            recs.width=0
                            recs.height=0
                            rotos+=1
            
        reloj1.tick(20)
        (r1.left,r1.top)=pygame.mouse.get_pos()
        r1.left-=r1.width/2
        r1.top-=r1.height/2
        pantalla.fill((0,0,45))
        pantalla.blit(texto1, (400,500))
        pantalla.blit(info, (0,40))
        if segundosint>=10:
            termino=True
        if termino==False:
            segundosint=pygame.time.get_ticks()/1000
            segundos=str(segundosint)
            contador=fuente1.render(segundos,0,(255,255,0))
        else:
            contador=fuente1.render(segundos+" Ud es un idiota por romper "+str(rotos),0,(255,255,0))
        for recs in listarec:
            pygame.draw.rect(pantalla,(0,200,0),recs)
        pygame.draw.rect(pantalla,(240,34,5),r1)
        pantalla.blit(contador, (0,450))
        pygame.display.update()

main()