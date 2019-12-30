import pygame
from pygame.locals import *
import os
import random
import time

# 拼接路径函数
def getPath(path):
    return os.path.join('E:\\python使用软件\\IT研究院-Python\\New_Stydy\\img\\',path)

class Biu_Plane():
    def __init__(self,x,y,windows):
        self.x = x
        self.y = y
        self.windows = windows

# 飞机
class Plane(Biu_Plane):
    def __init__(self, x, y, windows):
        super().__init__(x,y,windows)
        self.normalImageIndex = 0
        self.bulletList = []
        self.bombImageInedx = 0
        self.isBomb = False
    def draw(self):
        if not self.isBomb:
            image = pygame.image.load(
                getPath(self.normalImageList[self.normalImageIndex]))
            self.normalImageIndex = (self.normalImageIndex + 1) % len(
                self.normalImageList)
            self.windows.blit(image, (self.x, self.y))
        else:
            if self.bombImageInedx == len(self.bombImageList):
                time.sleep(0.3)
                exit(0)
            image = pygame.image.load(
                getPath(self.bombImageList[self.bombImageInedx]))
            self.windows.blit(image, (self.x, self.y))
            self.bombImageInedx += 1
            time.sleep(0.2)

class HeroPlane(Plane):
    def __init__(self, x, y, windows):
        super().__init__(x, y, windows)
        self.normalImageList = ['hero1.png', 'hero2.png']
        self.bombImageList = ['hero_blowup_n1.png', 'hero_blowup_n2.png',
                              'hero_blowup_n3.png', 'hero_blowup_n4.png']
    def draw(self):
        super().draw()
        self.rectT = Rect(self.x + 36, self.y, 28, 40)
        self.rectD = Rect(self.x, self.y + 40, 100, 84)
        for bullet in self.bulletList:
            bullet.draw()
            bullet.rect = Rect(bullet.x, bullet.y, 22, 22)
            if bullet.rect.colliderect(enemyPlane.rect):
                self.bulletList.remove(bullet)
                enemyPlane.isBomb = True
            else:
                self.bulletList.remove(bullet) if bullet.y <= 0 else ''
    def dealEvent(self, eventList):
        for event in eventList:
            if event.type == QUIT:
                exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.x = self.x - 5 if self.x > 5 else 0
                elif event.key == K_RIGHT:
                    self.x = self.x + 5 if self.x < 480 - 100 - 5 else 480 - 100
                elif event.key == K_SPACE:
                    bullet = HeroBiu(self.x + 100 // 2 - 22 // 2, self.y - 22,
                                     windows)
                    self.bulletList.append(bullet)

class EnemyPlane(Plane):
    def __init__(self, x, y, windows):
        super().__init__(x, y, windows)
        self.normalImageList = ['enemy1.png']
        self.bombImageList = ['enemy1_hit.png', 'enemy1_down1.png',
                              'enemy1_down2.png', 'enemy1_down3.png',
                              'enemy1_down4.png']
        self.directe = 'right'
    def draw(self):
        super().draw()
        if not self.isBomb:
            self.run()
            self.fire()
        self.rect = Rect(self.x, 0, 69, 89)
        for bullet in self.bulletList:
            bullet.draw()
            bullet.rect = Rect(bullet.x, bullet.y, 9, 21)
            if bullet.rect.colliderect(
                    heroPlane.rectT) or bullet.rect.colliderect(
                    heroPlane.rectD):
                self.bulletList.remove(bullet)
                heroPlane.isBomb = True
            else:
                self.bulletList.remove(bullet) if bullet.y >= 652 - 21 else ''
    def run(self):
        if self.directe == 'right':
            self.x += 1.7
            if self.x >= 480 - 69:
                self.directe = 'left'
        else:
            self.x -= 1.7
            if self.x <= 0:
                self.directe = 'right'
    def fire(self):
        h = random.randint(0, 100)
        if h == 3 or h == 67:
            bullet = EnemyBiu(self.x + 69 // 2 - 9 // 2, self.y + 89, windows)
            self.bulletList.append(bullet)

# 射击
class Biu(Biu_Plane):
    def draw(self):
        self.windows.blit(self.image, (self.x, self.y))
        self.move()  # 多态

class HeroBiu(Biu):
    def __init__(self, x, y, windows):
        super().__init__(x, y, windows)
        self.image = pygame.image.load(getPath('bullet.png'))
    def move(self):
        self.y -= 5

class EnemyBiu(Biu):
    def __init__(self, x, y, windows):
        super().__init__(x, y, windows)
        self.image = pygame.image.load(getPath('bullet2.png'))
    def move(self):
        self.y += 5

windows = pygame.display.set_mode((480, 652), 0, 32)
pygame.display.set_caption('飞机大战')
backGround = pygame.image.load(getPath('background.png'))
icon = pygame.image.load(getPath('icon72x72.png'))
pygame.display.set_icon(icon)
heroPlane = HeroPlane(480 // 2 - 100 // 2, 652 - 124, windows)
enemyPlane = EnemyPlane(480 // 2 - 69 // 2, 0, windows)
# 速度
# 第一个参数--按下键盘多少毫秒后开始反应
# 第二个参数--若不抬起，每多少毫秒再次触发按键
pygame.key.set_repeat(15, 15)

while True:
    windows.blit(backGround, (0, 0))
    enemyPlane.draw()
    heroPlane.draw()
    heroPlane.dealEvent(pygame.event.get())
    pygame.display.update()