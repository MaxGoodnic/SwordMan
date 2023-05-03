import pygame 

BLACK = (0, 0, 0) # цвет текста

#тексты, которые будут показаны в меню
font = pygame.font.SysFont('arial', 30)
start_label = font.render('Новая игра', 1, BLACK)
back_label = font.render('Вернуться к игре', 1, BLACK)
statistic_label = font.render('Статистика', 1, BLACK)
settings_label = font.render('Настройки управления', 1, BLACK)
menu_label = font.render('Вернуться в меню', 1, BLACK)
restart_label = font.render('Начать заново', 1, BLACK)
info1_label = font.render('Управление:', 1, BLACK)
info2_label = font.render('перемещение -- кнопки K_LEFT/K_RIGHT', 1, BLACK)
info3_label = font.render('прыжок -- кнопка K_SPACE', 1, BLACK)
info4_label = font.render('удар мечом -- кнопка K_a', 1, BLACK)
info5_label = font.render('выход в меню -- кнопка K_ESCAPE', 1, BLACK)