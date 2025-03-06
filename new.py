import pygame
from pygame.locals import *
pygame.init()
fpsclock = pygame.time.Clock()
FPS = 60
#variable
WINDOWWIDTH = 540
WINDOWHEIGHT = 540
width = 100
height = 100

#dir
dir_ = "thonny/game1/"

#img
ic = pygame.image.load(dir_ +'layla.jpg')
img1 = pygame.image.load(dir_ +'granger.png')
img2 = pygame.image.load(dir_ +'bg.jpg')
#screen
icon = pygame.display.set_icon(ic)
caption = pygame.display.set_caption("new")
screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))


class player():
    def __init__(self,hero_img,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hero = pygame.transform.scale(hero_img,(width,height))
        self.hero_rect = self.hero.get_rect(topleft = (self.x,self.y))
        self.hero_rect_ref = self.hero.get_rect(topleft = (self.x,self.y))
        self.speed = 10
        self.check = True
        self.jump = 0
        self.j = 0


    def draw(self,screen):
        screen.blit(self.hero,(self.hero_rect_ref.left,self.hero_rect_ref.top)) 
  

    def move(self,BG,up,down,left,right):
        self.hero_rect.centery += self.j
        if down:
            self.hero_rect.centery += self.speed
        if left:
            self.hero_rect.centerx -= self.speed
        if right:
            self.hero_rect.centerx += self.speed
    # biên
        if self.hero_rect.left < 0:
            self.hero_rect.left = 0
        if self.hero_rect.right > BG.bg.get_width():
            self.hero_rect.right = BG.bg.get_width()
        if self.hero_rect.top < 0:
            self.hero_rect.top = 0
        if self.hero_rect.bottom > BG.bg.get_height():
            self.hero_rect.bottom = BG.bg.get_height()
            player.jump = 0
            player.check = True
       # if player.jump == 3:
        #    player.check = False
        self.hero_rect_ref.left = self.hero_rect.left + BG.x
        self.hero_rect_ref.top = self.hero_rect.top + BG.y

class BG():
    def __init__(self,BG_IMG,x,y,WINDOWWIDTH,WINDOWHEIGHT):
        self.x = x
        self.y = y
        self.WINDOWWIDTH = WINDOWWIDTH
        self.WINDOWHEIGHT = WINDOWHEIGHT
        self.bg = pygame.transform.scale(BG_IMG,(1000,WINDOWHEIGHT))
        self.srcoll_x = 0
        self.srcoll_y = 0
        self.target_x = 0
        self.target_y = 0
    def draw(self,screen):
        screen.blit(self.bg,(self.x,self.y))
    
    def move(self,player):
        if player.hero_rect.right > WINDOWWIDTH - self.x:
            self.scroll_x = -player.speed
            self.x += self.scroll_x
        if player.hero_rect.left < -self.x:
            self.scroll_x = player.speed
            self.x += self.scroll_x
        if player.hero_rect.bottom > WINDOWHEIGHT - self.y:
            self.srcoll_y = -player.speed
            self.y += self.srcoll_y
        if player.hero_rect.top < -self.y:
            self.srcoll_y = player.speed
            self.y += self.srcoll_y
        '''
        target_x = WINDOWWIDTH // 2 - player.hero_rect.centerx
        target_y = WINDOWHEIGHT // 2 - player.hero_rect.centery

        self.scroll_x = (target_x - self.x) / 10
        self.scroll_y = (target_y - self.y) / 10

        self.x += self.scroll_x
        self.y += self.scroll_y
        '''
p = 1
running = True
up ,down ,left, right = False ,False ,False ,False 
player = player(img1,0,int(WINDOWHEIGHT - height),width,height)
BG = BG(img2,0,0,WINDOWWIDTH,WINDOWHEIGHT)
while running:
    BG.draw(screen)
    BG.move(player)
    player.draw(screen)
    player.move(BG,up,down,left,right)
    print(player.jump,'jump')
    print(player.check)
    print(player.j,'j')
    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
            running = False
        if event.type == KEYDOWN:
            if player.check: 
                if event.key == K_UP:
                    up = True
                    player.j = 0
                    player.j -= 18
                    player.jump +=1
                    if player.jump == 3:
                        player.check = False
            if event.key == K_DOWN:
                down = True
               # print("down")
            if event.key == K_LEFT:
                left = True
                #print("left")
            if event.key == K_RIGHT:
                right = True
                #print("right")
            if event.key == K_SPACE:
                running = False
        if event.type == KEYUP:
            if event.key == K_UP:
                up = False
            if event.key == K_DOWN:
                down = False
            if event.key == K_LEFT:
                left = False
            if event.key == K_RIGHT:
                right = False
    player.j += p
    pygame.display.update()
    fpsclock.tick(FPS)        
