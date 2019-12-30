import pygame
import random,time
from pygame.locals import *
import os

'''
#写一个getPath方法，在以后的调用中直接写一个文件名就可以了
显示飞机冒烟效果
实现飞机左右移动
实现飞机连续的发射子弹
'''
#写一个getPath方法，在以后的调用中直接写一个文件名就可以了
def getPath(path):
    return os.path.join("E:\\python使用软件\\IT研究院-Python\\New_Stydy\\img\\",path)
class Biu():
    def __init__(self,x,y,windows):
        self.x=x
        self.y=y
        self.windows=windows
        self.image=pygame.image.load(getPath("bullet.png"))

    def draw(self):
        self.windows.blit(self.image,(self.x,self.y))
        self.move()
    def move(self):
        self.y-=5
class HeroPlane():
    def __init__(self,x,y,windows):
        self.x=x
        self.y=y
        self.windows=windows#设置窗口，xy坐标
        self.heiht=124
        self.width=100
        #导入正常的飞机图片列表，以下实现飞机冒烟的效果
        self.normalImageList=['hero1.png','hero2.png']
        self.normalImageIndex=0#切换显示飞机图片
        self.biuList=[]
        self.isBomb = False
        self.bombImageList = ['hero_blowup_n1.png', 'hero_blowup_n2.png', 'hero_blowup_n3.png', 'hero_blowup_n4.png']
        self.bombImageIndex = 0

        # 碰撞检测:wo机和对方子弹
    def pzjc(self, bList):
        eRect = Rect(self.x, self.y, 100, 124)
        for zd in bList:
            zdRect = Rect(zd.x, zd.y, 9, 21)
            if zdRect.colliderect(eRect):
                self.isBomb = True
                bList.remove(zd)

    def draw(self):
        if not self.isBomb:
            image=pygame.image.load(getPath(self.normalImageList[self.normalImageIndex]))
            self.normalImageIndex=(self.normalImageIndex+1)%len(self.normalImageList)#切换飞机显示图片
            self.windows.blit(image,(self.x,self.y))
        else:
            if len(self.bombImageList)==self.bombImageIndex:
                time.sleep(0.5)
                exit(0)
            image=pygame.image.load(getPath(self.bombImageList[self.bombImageIndex]))
            self.bombImageIndex+=1
            self.windows.blit(image,(self.x,self.y))
            time.sleep(0.3)

        for zd in self.biuList:
            zd.draw()
            self.biuList.remove(zd) if zd.y < 0 else ''


    def dealEvent(self,evenList):
        for event in evenList:
            if event.type==QUIT:
                exit(0)
            elif event.type==KEYDOWN:
                if event.key==K_LEFT:
                   self.x=self.x-5 if self.x>5 else 0
                elif event.key==K_RIGHT:
                    self.x=self.x+5 if self.x<480-100-5 else 480-100
                elif event.key==K_SPACE:
                    zd=Biu(self.x+100//2-22//2,self.y-22,self.windows)
                    self.biuList.append(zd)
class EnemyBiu():
    def __init__(self,x,y,windows):
        self.x = x
        self.y = y
        self.windows = windows
        self.image=pygame.image.load(getPath("bullet2.png"))
    def draw(self):
        self.windows.blit(self.image,(self.x,self.y))
        self.move()
    def move(self):
        self.y+=3

class EnemyPlane():
    def __init__(self,x,y,windows):
        self.x=x
        self.y=y
        self.windows=windows
        self.height=89
        self.width =69
        self.normalImageList = ['enemy1.png']
        self.normalImageIndex = 0  # 切换显示飞机图片
        self.direct="左"
        self.enemyBiuList=[]
        self.isBomb=False
        self.bombImageList = ['enemy1_down1.png','enemy1_down2.png','enemy1_down3.png','enemy1_down4.png']
        self.bombImageIndex = 0
    def draw(self):
        if not self.isBomb:
            image = pygame.image.load(getPath(self.normalImageList[self.normalImageIndex]))
            self.normalImageIndex = (self.normalImageIndex + 1) % len(self.normalImageList)  # 切换飞机显示图片
            # image=pygame.image.load(getPath('enemy1.png'))
            self.windows.blit(image,(self.x,self.y))
            self.move()
            self.fire()
        else:
            if len(self.bombImageList)==self.bombImageIndex:
                time.sleep(0.5)
                exit(0)
            image=pygame.image.load(getPath(self.bombImageList[self.bombImageIndex]))
            self.bombImageIndex+=1
            self.windows.blit(image,(self.x,self.y))
            time.sleep(0.3)
        # for zd in self.biuList:
        #     zd.draw()
        for zd in self.enemyBiuList:
                zd.draw()
    def move(self):
        if self.direct=='左':
            self.x-=2
            if self.x<=0:
                self.direct='右'
        else:
            self.x+=2
            if self.x>=480-69:
                self.direct="左"
    def fire(self):
        h=random.randint(1,100)
        if h==3 or h==67:
            zd=EnemyBiu(self.x+69//2-9//2,self.y+89,windows)
            self.enemyBiuList.append(zd)
    #碰撞检测:敌机和对方子弹
    def pzjc(self,bList):
        eRect=Rect(self.x,self.y,69,89)
        for zd in bList:
            zdRect=Rect(zd.x,zd.y,22,22)
            if zdRect.colliderect(eRect):
                self.isBomb=True
                bList.remove(zd)



windows=pygame.display.set_mode((480,652),0,32)
pygame.display.set_caption("飞机大战")
#拼接路径
# x=os.path.join("E:\\python使用软件\\IT研究院-Python\\New_Stydy\\img\\",'background.png')
# print(x)
backGround=pygame.image.load(getPath('background.png'))
icon=pygame.image.load(getPath('icon72x72.png'))
pygame.display.set_icon(icon)
pygame.key.set_repeat(30,30)

heroPlane=HeroPlane(480//2-100//2,652-124,windows)
enemyPlane=EnemyPlane(480//2-69//2,0,windows)
while True:
    windows.blit(backGround,(0,0))
    heroPlane.draw()
    enemyPlane.draw()
    enemyPlane.pzjc(heroPlane.biuList)
    heroPlane.pzjc(enemyPlane.enemyBiuList)
    # enemyPlane.pzjc(HeroPlane.)
    heroPlane.dealEvent(pygame.event.get())
    pygame.display.update()