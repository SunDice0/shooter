#Створи власний Шутер!
import pygame
import random
import time
win_width = 700
win_height = 500

window = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("shooter")
FPS=pygame.time.Clock()
game=True
finish=False
lost=0
score=0

pygame.mixer.init()

pygame.mixer.music.load("space.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.7)
pygame.font.init()

class Settings:
    def __init__(self,image,x,y,w,h):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Player(Settings):
    def __init__(self,image,x,y,w,h,s,hp):
        super().__init__(image,x,y,w,h)
        self.speed = s
        self.hp = hp
        self.shoot=True
        self.image_heart = pygame.image.load("hp.png")
        self.image_heart=pygame.transform.scale(self.image_heart,(50,50))
    
    def move(self):
        global bullets
        self.show_heart()
        keys = pygame.key.get_pressed()
        if keys [pygame.K_a] and self.rect.x > 0:
            self.rect.x-=self.speed
        if keys [pygame.K_d] and self.rect.x < win_width-self.rect.width:
            self.rect.x+=self.speed
        if keys [pygame.K_w] and self.rect.y > 0:
            self.rect.y-=self.speed
        if keys [pygame.K_s] and self.rect.y < win_height-self.rect.height:
            self.rect.y+=self.speed
        if keys [pygame.K_SPACE] and self.shoot:
            bullets.append(Bullet(self.rect.centerx,self.rect.y,10,25,5))
            self.shoot=False
        
def show_heart(self):
    for h in range(self.hp):
        window.blit(self.image_heart,(win_width-50-h*50,0))

class Enemy(Settings):
    def __init__(self, image, x, y, w, h, s , hp):
        super().__init__(image, x, y, w, h)
        self.rect.x = random.randint(0,win_width-100)
        self.rect.y = random.randint(-300,-100)
        self.speed = s
        self.hp = hp

    def move(self):
        global lost
        for e in enemies:
            if self.rect.colliderect(e.rect) and self.rect !=e.rect:
                self.rect.x = random.randint(0,win_width-100)
                self.rect.y = random.randint(-300,-100)
        self.rect+=self.speed
        if self.rect.y>win_height:
            lost+=1
            self.rect.x = random.randint(0,win_width-100)
            self.rect.y = random.randint(-300,-100)
        for e in enemies:
            if self.rect.colliderect(e.rect) and self.rect !=e.rect:
                self.rect.x = random.randint(0,win_width-100)
                self.rect.y = random.randint(-300,-100)

class Label():
    def set_text(self,text,size,color=(255,255,255)):
        self.text=pygame.font.SysFont("veranda",size).render(text,True,color)

    def draw(self,x,y):
        window.blit(self.text,(x,y))

class Bullets():
    def __init__(self,x,y,w,h,s):
        self.rect=pygame.Rect(x,y,w,h)
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.speed=s

    def move1(self):
        global bullets,enemies
        self.rect.y-=self.speed
        if self.rect.y<0 and self in bullets:
            bullets.remove(self)
            for e in enemies:
                if self.rect.colliderect(e.rect)and self in bullets and e.hp>0:
                    e.hp-=1
                    bullets.remove(self)
                    score+=1


    def draw(self):
        pygame
        

fon=Settings("galaxe.jpg",0,0,win_width,win_height)
player=Player("rocket.png",win_width//2,win_height-100,100,100,10,5)
text_score=Label()
enemies=[]
bullets=[]
for i in range(5):
    enemies.append(Enemy("ufo.png",0,0,50,50,2,1))

while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if finish!=True:
            fon.draw()
            player.draw()
            player.move()
            text_score.set_text("Рахунок: "+str(score),20)
            text_score.draw(5,10    )
        for e in enemies:
            e.draw()
            e.move()
        for b in bullets:
            b.draw()
            b.move1()

        pygame.display.flip()
        FPS.tick(60)
