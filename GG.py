
import pygame
from pygame import font 
 
pygame.init()
 
schermata= pygame.display.set_mode ((550, 650)) #larghezza e altezza
# importa le immagini
sfondo = pygame.image.load('back.png')
ga =pygame.image.load('gaiadestra.png')
gio = pygame.image.load('giosinistra.png')
pavimento =pygame.image.load('base.png')
sparo =pygame.image.load('sparo.png')
sparogio=pygame.image.load('sparo2.png')
GAIA=pygame.image.load('ga.png')
GIO=pygame.image.load('gioo.png')                                   
v1=pygame.image.load('1vita.png')#vite
v2=pygame.image.load('2vite.png')
v3=pygame.image.load('3vite.png')


#inizializza i personaggi

count1= 0
count2= 0

def vite():
   global count1,count2
   if count2==0:
      schermata.blit(v3,(10,20)) 
   if count2==1:
      schermata.blit(v2,(10,20)) 
   if count2==2:
      schermata.blit(v1,(10,20))  
   if count1==0:
      schermata.blit(v3,(470,20)) 
   if count1==1:
      schermata.blit(v2,(470,20)) 
   if count1==2:
      schermata.blit(v1,(470,20)) 
   pygame.display.update()
   pygame.time.Clock().tick(300)




def indicazioni(): # scrive sullo schermo come ricominciare la partita
   font=pygame.font.SysFont("comicsansms", 14) #font e grandezza scritta
   space= font.render("Press SPACE to restart " , True, (255,211,67)) #cosa scrivere e di che colore
   schermata.blit(space,(200,140)) #stampa la scritta


def finega(): #cosa fare se vince gaia
  global count1, count2
  count1 = 0
  count2= 0
  schermata.blit(GAIA,(30,0))
  indicazioni()
  pygame.display.update()
  pygame.time.Clock().tick(60)
  while True:
     for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  #per chiudere
           pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #per ricominciare
           main()
               
 
def finegio(): #cosa fare se vince gio
   global count1,count2
   count1=0
   count2 = 0
   schermata.blit(GIO,(17,0))
   indicazioni()
   pygame.display.update()
   pygame.time.Clock().tick(60)
   while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT: #per chiudere
           pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #per ricominciare
           main()


def gaspara(): #come spara gaia
    global xga,yga,xgio,ygio,count1
    xsparo=xga+50
    while xsparo<=500: 
        for event in pygame.event.get():  #fa muovere l'avversario per schivare
           if event.type == pygame.KEYDOWN and event.key ==pygame.K_UP:
              ygio -=70
           if event.type == pygame.KEYDOWN and event.key ==pygame.K_RSHIFT:
              giospara()
           if event.type == pygame.KEYUP and event.key == pygame.K_UP:
              ygio +=70
        if xsparo == xgio and yga== ygio:
           count1 += 1
           xsparo= 700
           if count1 == 3:
              finega()
        disegna()
        schermata.blit(sparo,(xsparo-10,yga))
        pygame.display.update()
        pygame.time.Clock().tick(300)
        xsparo +=10   #sposta proiettile
    
   
def giospara(): #come spara gio
    global xga,yga,xgio,ygio,count2
    xsparogio=xgio-50
    while xsparogio>=0:
        for event in pygame.event.get():   #fa muovere l'avversario per schivare
           if event.type == pygame.KEYDOWN and event.key ==pygame.K_w:
              yga -=70
           if event.type == pygame.KEYDOWN and event.key ==pygame.K_f:
              gaspara()
           if event.type == pygame.KEYUP and event.key == pygame.K_w:
              yga +=70
        if xsparogio == xga and ygio== yga:
           count2+=1
           xsparogio=-200
           if count2 ==3:
              finegio() 
        disegna()
        schermata.blit(sparo,(xsparogio-10,ygio))
        pygame.display.update()
        pygame.time.Clock().tick(300)
        xsparogio -=10  #sposta il proiettile
    

def disegna(): #disegna sullo schermo tutti gli oggetti
   global xga,yga,xgio,ygio
   schermata.blit(sfondo,(0,0))
   schermata.blit(pavimento,(0,600))
   schermata.blit(gio,(xgio,ygio))
   schermata.blit(ga,(xga,yga))


#muoversi
def main():
   global xga,yga,xgio,ygio
   xga= 0
   yga =547
   xgio=500
   ygio=547
   while True:  
    keys = pygame.key.get_pressed()  # continua le azioni se il tasto si tiene premuto
    if keys[pygame.K_d]:
       if xga<490:
          xga+=10
       else:
          xga=500
    if keys[pygame.K_a]:
       if xga> 10:
          xga -=10
       else:
          xga=0     
    if keys[pygame.K_RIGHT]:
       if xgio<490:
          xgio +=10
       else:
          xgio=500
    if keys[pygame.K_LEFT]:
       if xgio> 10:
          xgio -=10
       else:
          xgio=0
    for event in pygame.event.get():  #fa le cose solo una volta
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
           yga -=70
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
           gaspara()
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
           yga +=70      
        if event.type == pygame.KEYDOWN and event.key ==pygame.K_UP:
           ygio -=70
        if event.type == pygame.KEYDOWN and event.key ==pygame.K_RSHIFT:
           giospara()
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
           ygio +=70  
        if event.type == pygame.QUIT:
           pygame.quit()
    disegna()
    vite()
    pygame.display.update()
    pygame.time.Clock().tick(40)


main()