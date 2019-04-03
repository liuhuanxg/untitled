import  pygame
from pygame.locals import  *
import random
import time

class Base():
    def __init__(self,x,y,windows):
        self.x=x
        self.y=y
        self.windows=windows
class Biu(Base):
    image='./img/bullet.png'
    def __init__(self,planeX,planeY,windows):
        super().__init__(planeY+50-11,planeY-22,windows)
    def display(self):
        biuImage=pygame.image.load(Biu.image)
        self.windows.blit(biuImage,(self.x,self.y))
        self.move_up()
    def  move_up(self):
        self.y-=5
class EnemyBiu(Base):
    image='./img/bullet.png'
    def __init__(self,planeX,planeY,windows):
        super().__init__(planeX+30,planeY+89,windows)
    def display(self):
        biuImage=pygame.image.load(EnemyBiu.image)
        self.windows.blit(biuImage,(self.x,self.y))
        self.move_down()
    def move_down(self):
        self.y+=5
class EnemyPlane(Base):
    normalStatusImage='./img/enemy1.png'
    bombStatusImageList=['./img/enemy1_down1.png','./img/enemy1_down2.png',
                         './img/enemy3_down3.png','./img/enemy1_down4.png']
    EnemyBiuList=[]
    def __init__(self,x,y,windows):
        super().__init__(x,y,windows)
        self.bombStatusIndex=0
        self.isBomb=0
        self.direction='右'

    def display(self):
      if self.isBomb==0:
          self.windows.blit(pygame.image.load(EnemyPlane.normalStatusImage),(self.x,self.y))
      else:
          if self.bombStatusIndex==len(EnemyPlane.bombStatusImageList):
              time.sleep(0.5)
              exit(0)
          self.windows.blit(pygame.image.load(EnemyPlane.bombStatusImageList[self.bombStatusIndex]),(self.x,self.y))
          self.bombStatusIndex+=1
          time.sleep(0.2)
      self.move()
      rd=random.randint(0,100)
      if rd==5 or rd==50:
          zd=EnemyBiu(self.x,self.y,windows)
          EnemyPlane.EnemyBiuList.append(zd)
      for  zd1 in EnemyPlane.EnemyBiuList:
          zd1.display()
          EnemyPlane.EnemyBiuList.remove(zd1) if  zd1.y>652 else''
    def   move(self):
        if self.direction=='右':
            self.x+=2
            if self.x>480-69:
                self.direction='左'
            elif self.direction=='左':
                self.x-=2
                if self.x<0:
                    self.direction='右'
    def pzjc(self,zdList):
        djjx=pygame.Rect(self.x,self.y,69,89)
        for zd in zdList:
            zdjx=pygame.Rect(zd.x,zd.y,22,22)
            if pygame.Rect.colliderect(djjx,zdjx):
                self.isBomb=1
                zdList.remove(zd)
class HeroPlane(Base):
    normalStatusImageList=['./img/hero1.png','./img/hero2.png']
    bombStatusImageList=['./img/hero_blowup_n1.png','./img/hero_blowup_n2.png',
                         './img/hero_blowup_n3.png' ,'./img/hero_blowup_n4.png']
    def __init__(self,x,y,windows):
        super().__init__(x,y,windows)
        self.normalStatusIndex=0
        self.bombStatusIndex=0
        self.isBomb=0
        self.biuList=[]
    def display(self):
        if self.isBomb==0:
            normalImage=pygame.image.load(HeroPlane.normalStatusImageList[self.bombStatusIndex])
            self.windows.blit(normalImage,(self.x,self.y))
            self.normalStatusIndex+=1
            if self.normalStatusIndex==len(HeroPlane.bombStatusImageList):
               self.normalStatusIndex=0
        elif self.isBomb==1:
               if self.bombStatusIndex==len(HeroPlane.bombStatusImageList):
                   time.sleep(0.5)
                   exit(0)
               self.windows.blit(pygame.image.load(HeroPlane.bombStatusImageList[self.bombStatusIndex]),(self.x,self.y))
               self.bombStatusIndex+=1
               time.sleep(0.2)
        for zd in self.biuList:
            zd.display()
            self.biuList.remove(zd)if zd.y<0 else''
    def move_left(self):
        self.x-=10
        if self.x<0:
            self.x=0
    def move_right(self):
        self.x += 10
        if self.x  >480:
            self.x = 480
    def move_down(self):
        self.y += 10
        if self.y > 652:
            self.x = 652
    def move_up(self):
        self.y-= 10
        if self.y < 0:
            self.y = 0
    def fire(self):
        zd=Biu(self.x,self.y,windows)
        self.biuList.append(zd)
    def pzjc(self,zdList):
        jtRecy=pygame.Rect(self.x+36,self.y,28,38)
        jsRect=pygame.Rect(self.x,self.y+38,100,97-38)
        for zd in zdList:
            zdRect=pygame.Rect(zd.x,zd.y,9,21)
            if pygame.Rect.colliderect(jtRecy,zdRect)or pygame.Rect.colliderect(jsRect,zdRect):
                self.isBomb=1
                zdList.remove(zd)
def kongzhi(plane):
    for event in pygame.event.get():
        if event.type==QUIT:
            exit(0)
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                plane.move_left()
            elif event.key==K_RIGHT:
                plane.move_right()
            elif event.key == K_UP:
                plane.move_up()
            elif event.key == K_DOWN:
                plane.move_down()
            elif event.key == K_SPACE:
                plane.fire()
windows=pygame.display.set_mode((480,652),0,32)
pygame.display.set_caption('哥是飞机大战')
pygame.display.set_icon(pygame.image.load('./img/icon72x72.png'))
bg=pygame.image.load('./img/background.png')
pygame.key.set_repeat(50,50)

heroPlane=HeroPlane(190,500,windows)
enemyPlane=EnemyPlane(210,0,windows)
while True:
    windows.blit(bg,(0,0))
    heroPlane.display()
    enemyPlane.display()
    enemyPlane.pzjc(heroPlane.biuList)
    heroPlane.pzjc(enemyPlane.EnemyBiuList)
    kongzhi(heroPlane)
    pygame.display.update()
