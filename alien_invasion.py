import sys

import pygame


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen_width=1200
    screen_height=800
    screen = pygame.display.set_mode((screen_width,screen_height),0,32)
    pygame.display.set_caption('Alien Invasion')

    # 设置背景色
    bg_color=(230,230,230)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                sys.exit()
        
        # 每次循环时都重绘屏幕
        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
