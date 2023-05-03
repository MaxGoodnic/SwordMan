import pygame
import enemy
from stats import Statistic, GameState
from hero import Hero
import records
import controls

pygame.init()
sc = pygame.display.set_mode((600, 360))
pygame.display.set_caption('SwordMan') # название игры
icon = pygame.image.load('images/icon.png').convert() #иконка игры
bg = pygame.image.load('images/background.jpg').convert() #оснвной background игры
menu = pygame.image.load('images/menu.jpg').convert() # основной background игры во время нахождения в меню

pygame.display.set_icon(icon)
statistic = Statistic('statistic.txt') # загружаем файл со статистикой
game_stat = GameState() # загружаем основную игровую статистику
hero = Hero(sc) # загружаем главного героя
ghosts = pygame.sprite.Group() # объявляем список обычных привидений
orange_ghosts = pygame.sprite.Group() # объявляем список оранжевых привидений

#объявление фиксированного временного промежутка между появлениями привидений
ghost_timer = pygame.USEREVENT + 1
orange_ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2000)
pygame.time.set_timer(orange_ghost_timer, 3000)

clock = pygame.time.Clock()

while True :
    controls.events(statistic, game_stat, ghost_timer, orange_ghost_timer, ghosts, orange_ghosts)
    controls.update_screen(sc, bg, game_stat, ghosts, orange_ghosts)
    controls.update_menu(game_stat, sc, menu, ghosts, orange_ghosts, statistic, hero)

    pygame.display.update()

    # фиксация FPS для большей плавности процесса
    clock.tick(30)