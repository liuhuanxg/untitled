import  sys
import  pygame
from  settings import  Settings
def run_game():
    #初始游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    # 设置背景的长宽
    pygame.display.set_caption('Alien Invasion')
   #设置背景颜色
    bg_color=(230,230,230)
    # 颜色设置（250,0,0）(0,250,0)(0,0,250)分别代表红绿蓝
    #开始游戏的主循环
    while True:
        #监视鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
#每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #让最近绘制的屏幕可见
    pygame.display.flip()
run_game()