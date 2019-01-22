import sys
import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建外星人的编组
    aliens = Group()
    # 创建一个外星人群
    gf.creat_fleet(ai_settings, screen, ship, aliens)
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更改飞船的位置
        ship.update()
        # 更新子弹的位置
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        # 更新外星人的位置
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
