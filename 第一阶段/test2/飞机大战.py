import  pygame
import  random
from pygame.locals import *
import time
class Biu():
    pic=pygame.image.load('./img/bullet.png')
    def __init__(self,fjx,fjy,windows):
       self.x=x+50-11
       self.y=y-19
       self.windows=windows
    def display(self):
        self.windows.blit(Biu.pic,(self.x,self.y))
        self.move()
    def move(self):
        self.y-=5
BiuList=[]


class EnemyBiu():
    pic=pygame.image.load('./img/bullet1.png')
    def __init__(self,djx,djy,windows):
       self.x=x1+30
       self.y=y1+89
       self.windows=windows
    def display(self):
        self.windows.blit(EnemyBiu.pic,(self.x,self.y))
        self.move()
    def move(self):
        self.y+=5
EnemyBiuList=[]

windows=pygame.display.set_mode((480,652),0,32)
pygame.display.set_caption('我是飞机大战')
icon=pygame.image.load('./img/icon72x72.png')  #加载图片
pygame.display.set_icon(icon)     #设置标题栏的图标

pygame.key.set_repeat(20,20)

# 我方战机爆炸瞬间
is_bomb=0
bombindex=0
bomb_image_list=['./img/hero_blowup_n1.png','./img/hero_blowup_n2.png',
                 './img/hero_blowup_n3.png','./img/hero_blowup_n4.png']

# 敌方战机爆炸瞬间
is_ebomb=0
ebombindex=0
ebomb_image_list=['./img/enemy1_down1.png','./img/enemy1_down2.png',
                 './img/enemy1_down3.png','./img/enemy1_down4.png']

background=pygame.image.load('./img/background.png')
hero1=pygame.image.load('./img/hero1.png')
hero2=pygame.image.load('./img/hero2.png')
heroPaint=1
enemy1=pygame.image.load('./img/enemy1.png')

wdzdx=0
wdzdy=0
fire=0


directory = '左'

x1=210
y1=0

x=(480-100)/2
y=500


while True:

    jtrect = pygame.Rect(x + 36, y, 28, 38)
    # 机头矩形
    jsrect = pygame.Rect(x, y + 38, 100, 97 - 38)
    # 机身的矩形
    for ezdpz in EnemyBiuList:  #每颗子弹矩形
        ezdrect = pygame.Rect(ezdpz.x, ezdpz.y, 9, 21)
        if pygame.Rect.colliderect(ezdrect, jsrect) or pygame.Rect.colliderect(ezdrect, jtrect):
            is_bomb= 1
            EnemyBiuList.remove(ezdpz)
            break
    djrect=pygame.Rect(x1,y1,69,89)#敌机子弹的矩形
    for wdzdpz in BiuList:  # 每颗敌方子弹矩形
        wdzdrect = pygame.Rect(wdzdpz.x, wdzdpz.y,22, 22)     # 我方子弹的矩形
        if pygame.Rect.colliderect(wdzdrect, djrect):      #判断矩形相交时候
            is_ebomb = 1
            BiuList.remove(wdzdpz)
            break
    windows.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type==QUIT:
            exit(0)
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                x-=10
                if x<0:
                    x=0
            elif event.key==K_RIGHT:
                x+=10
                if x>380:
                    x=380
            elif event.key==K_UP:
                y-=10
                if y<0:
                 y=0
            elif event.key == K_DOWN:
                y += 10
                if y >528:
                   y = 528
            elif event.key==K_SPACE:
              one=Biu(x,y,windows)
              BiuList.append(one)

    for zd in BiuList:
        zd.display()
        if zd.y<0:
            BiuList.remove(zd)
            # Biulist.remove(zd)if zd.y<0 else""

    sjs= random.randint(0, 100)
    if sjs == 30 or sjs == 50:
        one=EnemyBiu(x,y,windows)
        EnemyBiuList.append(one)
    for ezd in EnemyBiuList:
        ezd.display()
        if ezd.y>=625:
            EnemyBiuList.remove(ezd)

    if is_bomb == 0:
        if heroPaint == 1:
            windows.blit(hero1, (x, y))
            heroPaint = 2
        elif heroPaint == 2:
            windows.blit(hero2, (x, y))
            heroPaint = 1
    elif is_bomb == 1:
        time.sleep(0.5)
        if bombindex == 4:
            time.sleep(0.5)
            exit(0)
        bomimage = pygame.image.load(bomb_image_list[bombindex])
        windows.blit(bomimage, (x, y))
        bombindex += 1
    if directory=='左':
        x1-=1
        if x1<=0:
            directory='右'
    elif directory=='右':
        x1+=1
        if x1>=480-69:
            directory='左'

    if is_ebomb == 0:
        windows.blit(enemy1, (x1, y1))
    elif is_ebomb == 1:
        time.sleep(0.5)
        if ebombindex == 4:
            time.sleep(0.5)
            exit(0)
        ebomimage = pygame.image.load(bomb_image_list[ebombindex])
        windows.blit(ebomimage, (x1, y1))
        ebombindex += 1

    pygame.display.update()