import pygame
import stats
import enemy
import records

#Числовые константы
DisplayWidth = 600
DisplayHeight = 360
BLACK = (0,0,0)

def events(statistic, game_stat, ghost_timer, orange_ghost_timer, ghosts, orange_ghosts):
    """считывание нажатия кнопки выхода и добавление привидений по счётчику"""
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            if game_stat.get_stat()[2] :
                statistic.file_write(game_stat.get_score())
            exit()
        if event.type == ghost_timer and game_stat.get_stat()[5] :
            enemy.create_ghost(ghosts)
        if event.type == orange_ghost_timer and game_stat.get_stat()[5] :
            enemy.create_orange_ghost(orange_ghosts)

def collide_ghosts(hero, group, game_stat, statistic, ghosts, orange_ghosts):
    """считывание касания обычного привидения и героя с его мечом"""
    for ghost in group:
        if hero.rect.colliderect(ghost.rect):
            game_stat.set_lose()            
            ghosts.empty()
            orange_ghosts.empty()
            hero.zeroing()
            enemy.Ghost.count_zeroing()
            enemy.OrangeGhost.count_zeroing()
            statistic.file_write(game_stat.get_score())
            game_stat.add_score(-game_stat.get_score())
        elif hero.sword.colliderect(ghost.rect) :
            game_stat.add_score(ghost.score)
            ghost.kill()

def collide_orange_ghosts(hero, group, game_stat, statistic, ghosts, orange_ghosts):
    """считывание касания оранжевого привидения и героя"""
    for orange_ghost in group:
        if hero.rect.colliderect(orange_ghost.rect):
            game_stat.set_lose()
            statistic.file_write(game_stat.get_score())
            game_stat.add_score(-game_stat.get_score())
            ghosts.empty()
            orange_ghosts.empty()
            hero.zeroing()
            enemy.Ghost.count_zeroing()
            enemy.OrangeGhost.count_zeroing()

def update_menu(game_stat, sc, menu, ghosts, orange_ghosts, statistic, hero) :
    """отслеживание перемещения по вкладкам меню"""
    mouse = pygame.mouse.get_pos() 
    if game_stat.get_stat()[0] : # начальное меню
        sc.blit(menu, (0,0))
        pos1 = records.start_label.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2 - 60))
        pos2 = records.settings_label.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2))
        pos3 = records.statistic_label.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2 + 60))
        sc.blit(records.start_label, pos1)
        sc.blit(records.settings_label,pos2)
        sc.blit(records.statistic_label,pos3)
        if pos1.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            game_stat.set_game()
        elif pos2.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            game_stat.set_settings()
        elif pos3.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            game_stat.set_statistic()
    if game_stat.get_stat()[1] : # меню поражения
        sc.blit(menu, (0,0))
        pos1 = records.restart_label.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2 - 30))
        pos2 = records.menu_label.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2 + 30))
        sc.blit(records.restart_label, pos1)
        sc.blit(records.menu_label,pos2)
        if pos1.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            game_stat.set_game()
        elif pos2.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            game_stat.set_begin()
    if game_stat.get_stat()[2]: # меню паузы
        sc.blit(menu, (0,0))
        pos1 = records.back_label.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2 - 35))
        pos2 = records.menu_label.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2 + 35))
        sc.blit(records.back_label, pos1)
        sc.blit(records.menu_label,pos2)
        if pos1.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            game_stat.set_game()
        elif pos2.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            game_stat.set_begin()
            statistic.file_write(game_stat.get_score())
            game_stat.add_score(-game_stat.get_score())
            ghosts.empty()
            orange_ghosts.empty()
            hero.zeroing()
            enemy.Ghost.count_zeroing()
            enemy.OrangeGhost.count_zeroing()
    if game_stat.get_stat()[3]:  # меню настроек
        sc.blit(menu, (0,0))
        pos1 = records.info1_label.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2 - 75))
        pos2 = records.info2_label.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2 - 45))
        pos3 = records.info3_label.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2 - 15))
        pos4 = records.info4_label.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2 + 15))
        pos5 = records.info5_label.get_rect(center = (DisplayWidth // 2, DisplayHeight //2 + 45))
        pos6 = records.menu_label.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2 + 90))
        sc.blit(records.info1_label, pos1)
        sc.blit(records.info2_label, pos2)
        sc.blit(records.info3_label, pos3)
        sc.blit(records.info4_label, pos4)
        sc.blit(records.info5_label, pos5)
        sc.blit(records.menu_label,pos6)
        if pos6.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            game_stat.set_begin()
    if game_stat.get_stat()[4] : # меню статистики
        best_stata,last_stata = statistic.file_read(records.font, BLACK)
        pos1 = best_stata.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2 - 40))
        pos2 = last_stata.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2))
        pos3 = records.menu_label.get_rect(center = (DisplayWidth // 2, DisplayHeight // 2 + 100))
        sc.blit(menu, (0,0))
        sc.blit(best_stata, pos1)
        sc.blit(last_stata, pos2)
        sc.blit(records.menu_label, pos3)
        if pos3.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            game_stat.set_begin()
    if game_stat.get_stat()[5] : # процесс игры
        hero.update(sc, game_stat)
        ghosts.update()
        orange_ghosts.update()
        collide_ghosts(hero, ghosts, game_stat, statistic, ghosts, orange_ghosts)
        collide_orange_ghosts(hero, orange_ghosts, game_stat, statistic, ghosts, orange_ghosts)

def update_screen(sc, bg, game_stat, ghosts, orange_ghosts) :
    """отрисовка экрана во время игры"""
    if game_stat.get_stat()[5] :
        sc.blit(bg, (0,0))
        sc_text = records.font.render(str(game_stat.get_score()), 1, (94, 138, 14))
        sc.blit(sc_text, (20, 10))
        ghosts.draw(sc)
        orange_ghosts.draw(sc)