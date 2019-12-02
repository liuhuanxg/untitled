import pygame
from pygame.locals import *
import random, time


# 我方子弹
class Biu():
    def __init__(self, x, y, wind):
        self.x = x
        self.y = y
        self.wind = wind
        self.pic = pygame.image.load(r'D:\python0715\first\week4\day1-进程线程协程\img\bullet.png')

    def draw(self):
        self.wind.blit(self.pic, (self.x, self.y))
        self.move()

    def move(self):
        self.y -= 5


# 敌机子弹
class EnemyBiu:
    def __init__(self, x, y, wind):
        self.x = x
        self.y = y
        self.wind = wind
        self.pic = pygame.image.load(r'D:\python0715\first\week4\day1-进程线程协程\img\bullet1.png')

    def draw(self):
        self.wind.blit(self.pic, (self.x, self.y))
        self.move()

    def move(self):
        self.y += 5


wind = pygame.display.set_mode((480, 652), 0, 32)
background = pygame.image.load(r'D:\python0715\first\week4\day1-进程线程协程\img\background.png')
icon = pygame.image.load(r'D:\python0715\first\week4\day1-进程线程协程\img\icon72x72.png')
heroPlan1 = pygame.image.load(r'D:\python0715\first\week4\day1-进程线程协程\img\hero1.png')
heroPlan2 = pygame.image.load(r'D:\python0715\first\week4\day1-进程线程协程\img\hero2.png')
heroBombImageList = [r'D:\python0715\first\week4\day1-进程线程协程\img\hero_blowup_n1.png',
                     r'D:\python0715\first\week4\day1-进程线程协程\img\hero_blowup_n2.png',
                     r'D:\python0715\first\week4\day1-进程线程协程\img\hero_blowup_n3.png',
                     r'D:\python0715\first\week4\day1-进程线程协程\img\hero_blowup_n4.png']
enemyPlan = pygame.image.load(r'D:\python0715\first\week4\day1-进程线程协程\img\enemy1.png')

# 窗口名
pygame.display.set_caption('飞机大战')
# 窗口图标
pygame.display.set_icon(icon)
# 速度
# 第一个参数--按下键盘多少毫秒后开始反应
# 第二个参数--若不抬起，每多少毫秒再次触发按键
pygame.key.set_repeat(15, 15)

hero_x = (480 - 100) // 2
hero_y = 652 - 124
enemy_x = (480 - 69) // 2
enemy_direct = 'right'
hero_bullets = []
enemy_bullets = []
heroIndex = 0
heroPlaneIsBomb = False
heroBombImageIndex = 0
while True:
    wind.blit(background, (0, 0))
    if heroPlaneIsBomb == False:
        if heroIndex == 0:
            wind.blit(heroPlan1, (hero_x, hero_y))
            heroIndex = 1
        else:
            wind.blit(heroPlan2, (hero_x, hero_y))
            heroIndex = 0
    else:
        if heroBombImageIndex == len(heroBombImageList):
            time.sleep(0.2)
            exit(0)
        pic = pygame.image.load(heroBombImageList[heroBombImageIndex])
        wind.blit(pic, (hero_x, hero_y))
        heroBombImageIndex += 1
        time.sleep(0.1)
    wind.blit(enemyPlan, (enemy_x, 0))
    enemy_Rect = Rect(enemy_x, 0, 69, 89)
    hero_RectT = Rect(hero_x + 36, hero_y, 28, 40)
    hero_RectD = Rect(hero_x, hero_y + 40, 100, 84)
    for bullet in hero_bullets:
        bullet.draw()
        bullet_Rect = Rect(bullet.x, bullet.y, 22, 22)
        if enemy_Rect.colliderect(bullet_Rect):
            hero_bullets.remove(bullet)
        else:
            hero_bullets.remove(bullet) if bullet.y < 0 else ''
    # 循环获取事件（尤其是鼠标键盘事件）
    for event in pygame.event.get():
        # 如果事件的类型是退出（点击退出按钮触发）
        if event.type == QUIT:
            print('退出游戏')
            exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                hero_x = hero_x - 5 if hero_x > 5 else 0
            elif event.key == K_RIGHT:
                hero_x = hero_x + 5 if hero_x < 480 - 100 - 5 else 480 - 100
            elif event.key == K_UP:
                hero_y = hero_y - 10 if hero_y > 10 else 0
            elif event.key == K_DOWN:
                hero_y = hero_y + 10 if hero_y < 652 - 124 - 10 else 652 - 124
            elif event.key == K_SPACE:
                bullet = Biu(hero_x + 100 // 2 - 22 // 2, hero_y - 22, wind)
                hero_bullets.append(bullet)
    if enemy_direct == 'right':
        enemy_x += 1.7
        if enemy_x >= 480 - 69:
            enemy_direct = 'left'
    else:
        enemy_x -= 1.7
        if enemy_x <= 0:
            enemy_direct = 'right'
    h = random.randint(0, 100)
    if h == 3 or h == 67:
        enemybullet = EnemyBiu(enemy_x + 69 // 2 - 9 // 2, 89, wind)
        enemy_bullets.append(enemybullet)
    for enemybullet in enemy_bullets:
        enemybullet.draw()
        enemybullet_Rect = Rect(enemybullet.x, enemybullet.y, 9, 21)
        if hero_RectT.colliderect(enemybullet_Rect) or hero_RectD.colliderect(enemybullet_Rect):
            enemy_bullets.remove(enemybullet)
            heroPlaneIsBomb = True
        else:
            enemy_bullets.remove(enemybullet) if enemybullet.y > 652 - 21 else ''
    pygame.display.update()
