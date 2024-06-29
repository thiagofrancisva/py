import pygame
from time import localtime, strftime
#import comando
pygame.init()

goblin_life = 20
warrior_life = 30
attack = 10
revenge = 5
pausa = False
movimento = 0
ataque = 0
warcoolmin = -100
warcoolsec = -100
warriormin = 0
warriorsec = 0

gobcoolmin = int(strftime("%M",localtime()))
gobcoolsec = int(strftime("%S",localtime()))
x = 200
y = 261

volta = 0

janela = pygame.display.set_mode((800,600))

text = pygame.font.SysFont("arial",12)

goblin = pygame.image.load("goblin.png")
guerreiro = pygame.image.load("guerreiro.png")


goblin = pygame.transform.scale(goblin,(77, 81))
guerreiro = pygame.transform.scale(guerreiro,(120,120))

def contagem(seg,font,cor,x,y):
    img = font.render(seg,True,cor)
    janela.blit(img,(x,y))
    
janela_aberta = True
while janela_aberta:
    #pygame.time.delay(300)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comando=pygame.key.get_pressed()

    if comando[pygame.K_RIGHT]:
        x+=10
        
    if comando[pygame.K_LEFT]:
        x-=10

    #if comando[pygame.K_UP]:
        
    #if comando[pygame.K_DOWN]:
    warriormin = int(strftime("%M",localtime()))
    warriorsec = int(strftime("%S",localtime()))
    #print(warriormin)
    #print(warriorsec)
    
    if warriormin == warcoolmin and warriorsec > warcoolsec:
        if comando[pygame.K_a]:
            goblin_life -= attack
            warcoolmin = warriormin 
            warcoolsec = warriorsec + 5
        if comando[pygame.K_b]:
            goblin_life -= revenge
            warcoolmin = warriormin 
            warcoolsec = warriorsec + 5
    elif warriormin > warcoolmin and warriorsec > warcoolsec % 60:
        if comando[pygame.K_a]:
            goblin_life -= attack
            warcoolmin = warriormin 
            warcoolsec = warriorsec + 5
        elif comando[pygame.K_b]:
            goblin_life -= revenge
            warcoolmin = warriormin 
            warcoolsec = warriorsec + 5
    
    elif  warriorsec > warcoolsec:
        if comando[pygame.K_a]:
            goblin_life -= attack
            warcoolmin = warriormin 
            warcoolsec = warriorsec + 5
        elif comando[pygame.K_b]:
            goblin_life -= revenge
            warcoolmin = warriormin 
            warcoolsec = warriorsec + 5
    #elif movimento == 5:
        #movimento = 0
        #pausa = False
        
    #else:
        #movimento += 1

    #ataque += 1
    #if ataque == 5:
        #warrior_life -= 7
        #ataque = 0


    contagem("10",text,(255,255,255),200,400)
    
    if goblin_life <= 0:
        janela.fill((135,206,235))
    else:
        janela.fill((0,0,0))
        #pygame.draw.rect(janela,(152,251,152),pygame.Rect(600,380,30,20))
    
    #else:
    #    pygame.draw.rect(janela,(152,251,152),pygame.Rect(600,370,20,30))


    if warrior_life <= 0:
        janela.fill((255,0,0))
        
    #else:
        #pygame.draw.rect(janela,(192,192,192),pygame.Rect(200,330,30,70))
    
    janela.blit(guerreiro,(x,y))
    janela.blit(goblin,(600,300))
    
    pygame.display.update()

pygame.quit()
