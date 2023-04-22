import pygame
from random import randint
from ghost import Ghost




#Логические константы
pause = False #показывает, что паузу
game = False #показывает, что сейчас иигра активна
begin = True #показывает, что сейчас начальное мнею
settings = False #показывает, что сейчас меню настроек
statistic = False #показывает,что сейчас меню статистики
lose = False #показывает, что сейчас меню проигрыша

is_jump = False #показывает, что персонаж в процессе полёта
right = True #показывает, что персонаж смотрит вправо
move = False #показывает, что персонаж в процессе выполнения сложного движения

#Числовые константы
black = (0, 0, 0) # цвет текста
d_w = 600 # ширина экрана
d_h = 360 # высота экрана
FPS = 20 
const = 264 # уровень пола по оси Oy
speed = 7 # скорость персонажа
width = 76 # ширина персонажа в обычной стойке
jump_count = 8 # константа высоты прыжка персонажа
hero_x = 20 # начальное положение перонажа по оси Ox
hero_y = const # начальное положение персонажа по оси Oy
x = hero_x
y = hero_y
count = 0 # показывает, какой номер изображения персонажа брять во время ходьбы
step = 0 # показывает, какой номер изображения персонажа брять во время сложного движения
game_score = 0 # показывает текущий рекорд персонажа за забег

pygame.init()

sc = pygame.display.set_mode((d_w, d_h))
pygame.display.set_caption('SwordMan')

icon = pygame.image.load('images/icon.png').convert() #иконка игры
bg = pygame.image.load('images/background.jpg').convert() #оснвной background игры
menu = pygame.image.load('images/menu.jpg').convert() # основной background игры во время нахождения в меню

pygame.display.set_icon(icon)

#массив изображений персонажа, направленных вправо(ходьба)
hero_walk_right = [
    pygame.image.load('images/hero/steps/pos6.png').convert_alpha(),
    pygame.image.load('images/hero/steps/pos7.png').convert_alpha(),
    pygame.image.load('images/hero/steps/pos8.png').convert_alpha(),
    pygame.image.load('images/hero/steps/pos9.png').convert_alpha(),
    pygame.image.load('images/hero/steps/pos10.png').convert_alpha(),
    pygame.image.load('images/hero/steps/pos11.png').convert_alpha()
]
#массив изображений персонажа, направленных влево(ходьба)
hero_walk_left = [0] * 6
for i in range(6) :
    hero_walk_left[i] = pygame.transform.flip(hero_walk_right[i], 1, 0)
#массив изображений персонажа, направленных вправо(сложное движение)
hero_move_right = [
    pygame.image.load('images/hero/move/pos21.png').convert_alpha(),
    pygame.image.load('images/hero/move/pos22.png').convert_alpha(),
    pygame.image.load('images/hero/move/pos23.png').convert_alpha(),
    pygame.image.load('images/hero/move/pos24.png').convert_alpha(),
    pygame.image.load('images/hero/move/pos25.png').convert_alpha()
]
#массив изображений персонажа, направленных влево(сложное движение)
hero_move_left = [0] * 5
for i in range(5) :
    hero_move_left[i] = pygame.transform.flip(hero_move_right[i], 1, 0)

#объявление основного врага -- привидения и класса, характеризующего группу привидений
ghost = pygame.image.load('images/ghost.png').convert_alpha()
ghosts = pygame.sprite.Group()

#тексты, которые будут показаны в меню
font = pygame.font.SysFont('arial', 34)
start_label = font.render('Новая игра', 1, black)
back_label = font.render('Вернуться к игре', 1, black)
statistic_label = font.render('Статистика', 1, black)
settings_label = font.render('Настройки управления', 1, black)
menu_label = font.render('Вернуться в меню', 1, black)
restart_label = font.render('Начать заново', 1, black)

#объявление фиксированного временного промежутка между появлениями привидений
pygame.time.set_timer(pygame.USEREVENT, 4000)
clock = pygame.time.Clock()

# функция, добавляющая приведение в конретную группу привидений
def createGhost(group):
    x = 620
    speed = 10
    score = 1
    return Ghost(x, speed, ghost, score, group)

# проверка того, что персонаж перепрыгнул через привидение, и предоставление награды за это
def collideGhosts():
    global game, lose, game_score
    for ghost in ghosts:
        if hero_rect.colliderect(ghost.rect):
            game = False
            lose = True
        elif sword_rect.colliderect(ghost.rect) :
            game_score += ghost.score
            ghost.kill()


#работа с текстовым файлом "statistic.txt" для записи на 1-й строке рекордного результата 
# и на 2-й строке последнего результата забега
def statistic_write(file) :
    with open(file, "r") as f :
        best = int(f.readline()[:-1])
        last = int(f.readline())
    with open(file, 'w') as f:
        f.write(str(max(best, game_score)) + '\n')
        f.write(str(game_score))

#53 ширина 92 высота

#sword_rect = pygame.Rect(0,0,1,1)
#sword = pygame.Surface((60,92))
#sword.fill((0, 0, 255))
#тело программы - бесконечный цикл
while True :
    #считываем положение мыши для работы с кнопками в меню
    mouse = pygame.mouse.get_pos() 
    # рассматриваем все комбинации, напечатанные на клавиатуре и с помощью мыши, а конкретно 
    # выход из программы и добавление пришельцев по таймингу
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            statistic_write('statistic.txt')
            exit()
        if event.type == pygame.USEREVENT and game :
            createGhost(ghosts)
    #работа с начальной вкладкой меню: можно начать игру, зайти в настройки или посмотреть статистику 
    if begin :
        sc.blit(menu, (0,0))
        pos1 = start_label.get_rect(center = (d_w // 2, d_h // 2 - 50))
        pos2 = settings_label.get_rect(center = (d_w // 2, d_h // 2))
        pos3 = statistic_label.get_rect(center = (d_w // 2, d_h // 2 + 50))
        sc.blit(start_label, pos1)
        sc.blit(settings_label,pos2)
        sc.blit(statistic_label,pos3)
        if pos1.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            game = True
            begin = False
        elif pos2.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            settings = True
            begin = False
        elif pos3.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            statistic = True
            begin = False
    #работа с вкладкой настройки: можно псмотреть основные настройки и вернуться в начальное меню
    if lose :
        ghosts.empty()
        is_jump = False
        jump_count = 8
        hero_x = 20
        hero_y = const
        move = False
        right = True
        statistic_write('statistic.txt')
        sc.blit(menu, (0,0))
        pos1 = restart_label.get_rect(center = (d_w // 2, d_h // 2 - 50))
        pos2 = menu_label.get_rect(center = (d_w // 2, d_h // 2 + 50))
        sc.blit(restart_label, pos1)
        sc.blit(menu_label,pos2)
        if pos1.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            game = True
            lose = False
        elif pos2.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            begin = True
            lose = False
    if settings :  
        sc.blit(menu, (0,0))
        info1_label = font.render('Управление:', 1, black)
        info2_label = font.render('перемещение -- кнопки K_LEFT/K_RIGHT', 1, black)
        info3_label = font.render('прыжок -- кнопка K_SPACE', 1, black)
        info4_label = font.render('удар мечом -- кнопка K_x', 1, black)
        info5_label = font.render('выход в меню -- кнопка K_ESCAPE', 1, black)
        pos1 = info1_label.get_rect(center = (d_w // 2, d_h // 2 - 75))
        pos2 = info2_label.get_rect(center = (d_w // 2, d_h // 2 - 45))
        pos3 = info3_label.get_rect(center = (d_w // 2, d_h // 2 - 15))
        pos4 = info4_label.get_rect(center = (d_w // 2, d_h // 2 + 15))
        pos5 = info5_label.get_rect(center = (d_w // 2, d_h //2 + 45))
        pos6 = menu_label.get_rect(center = (d_w // 2, d_h // 2 + 75))
        sc.blit(info1_label, pos1)
        sc.blit(info2_label, pos2)
        sc.blit(info3_label, pos3)
        sc.blit(info4_label, pos4)
        sc.blit(info5_label, pos5)
        sc.blit(menu_label,pos6)
        if pos6.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            settings = False
            begin = True
    #работа с вкладкой меню пауза: можно вернуться в игру или выйти из игры в начальное меню
    if pause :
        sc.blit(menu, (0,0))
        pos1 = back_label.get_rect(center = (d_w // 2, d_h // 2 - 40))
        pos2 = menu_label.get_rect(center = (d_w // 2, d_h // 2 + 40))
        sc.blit(back_label, pos1)
        sc.blit(menu_label,pos2)
        if pos1.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            game = True
            pause = False
        elif pos2.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            statistic_write('statistic.txt')
            begin = True
            pause = False
    #работа с вкладкой меню сатистики: можно ознакомиться с рекордом и последним результатом забега или вернуться в начальное меню
    if statistic :
        with open('statistic.txt', 'r') as f :
            best_stata = font.render('Лучший счёт' + f.readline()[:-1], 1, black)
            last_stata = font.render('Последний счёт' +  f.readline(), 1, black)
        pos1 = best_stata.get_rect(center = (d_w // 2, d_h // 2 - 40))
        pos2 = last_stata.get_rect(center = (d_w // 2, d_h // 2))
        pos3 = menu_label.get_rect(center = (d_w // 2, d_h // 2 + 100))
        sc.blit(menu, (0,0))
        sc.blit(best_stata, pos1)
        sc.blit(last_stata, pos2)
        sc.blit(menu_label, pos3)
        if pos3.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            begin = True
            statistic = False
    #работа с вкладкой игры: можно ходить влево/право, прыгать, использовать сложное движение(взмах мечом) или выйти в меню паузы
    if game :
        sc.blit(bg, (0,0))
        keys = pygame.key.get_pressed()
        # сложное движение: взмах мечом, состоит из 5 движений, совершаемые в определенной последовательности, 
        # непрерываемое(из-за различия изображений приходится накладывать какие-то ограничения на координаты по оси x и y
        # так, чтобы процесс игры казался более плавным)
        if move and right and step != 0:
            x = hero_x
            y = hero_y - hero_move_right[step].get_height()
            sc.blit(hero_move_right[step], (x, y))
            step = (step + 1) % 5
            if step == 0 :
                move = False
        elif move and (not right) and step != 0 :
            x = hero_x
            y = hero_y - hero_move_right[step].get_height()
            sc.blit(hero_move_left[step], (x + hero_walk_right[count - 1].get_width() - hero_move_right[step].get_width(), y))
            step = (step + 1) % 5
            if step == 0 :
                move = False
        elif keys[pygame.K_a] and right:
            x = hero_x
            y = hero_y - hero_move_right[step].get_height()
            sc.blit(hero_move_right[step], (x, y))
            step = (step + 1) % 5
            move = True
        elif keys[pygame.K_a] :
            x = hero_x
            y = hero_y - hero_move_right[step].get_height()
            sc.blit(hero_move_left[step], (x + hero_walk_right[count - 1].get_width() - hero_move_right[step].get_width(), y))
            step = (step + 1) % 5
            move = True
        # обычное движение влево
        elif keys[pygame.K_LEFT] and hero_x > 0:
            hero_x -= speed
            x = hero_x
            y = hero_y - hero_walk_right[count].get_height()
            sc.blit(hero_walk_left[count], (x, y))
            count = (count + 1) % 6
            right = False
        
        # обычное движение вправо
        elif keys[pygame.K_RIGHT] and hero_x < d_w - 90:
            hero_x += speed
            x = hero_x
            y = hero_y - hero_walk_right[count].get_height()
            sc.blit(hero_walk_right[count], (x, y))
            count = (count + 1) % 6
            right = True
        # фиксированная стойка персонажа(смотрит влево или вправо)
        elif right: 
            x = hero_x
            y = hero_y - hero_walk_right[count].get_height()
            sc.blit(hero_walk_right[count], (x, y))
        else : 
            x = hero_x
            y = hero_y - hero_walk_right[count].get_height()
            sc.blit(hero_walk_left[count], (x, y))

        # выход в меню паузы
        if keys[pygame.K_ESCAPE] :
            pause = True
            game = False

        # работа над прыжком 
        if not is_jump :
            if keys[pygame.K_SPACE] :
                is_jump = True
        else :
            if jump_count >= -8 :
                if jump_count > 0 :
                    hero_y -= (jump_count ** 2) / 2
                    y -= (jump_count ** 2) / 2
                else :
                    hero_y += (jump_count ** 2) / 2
                    y += (jump_count ** 2) / 2
                jump_count -= 1
            else :
                is_jump = False
                jump_count = 8
        #обновление списка призраков
        ghosts.update()
        #sc.blit(sword,sword_rect)
        collideGhosts()
        # задание фиксированного прямоугольника, связанного с персонажем, для фиксирования прохождения препятствий
        if right : 
            hero_rect = pygame.Rect(x + 10, y, 53, 92)
            if move and step > 1 and step < 4 :
                sword_rect = pygame.Rect(x + hero_move_right[step].get_width() - 60, y, 60, 92) 
            else :
                sword_rect = pygame.Rect(0,0,1,1) 
        else : 
            if move :
                hero_rect = pygame.Rect(x, y, 53, 92)
                if step > 1 and step < 4 :
                    sword_rect = pygame.Rect(x + hero_walk_right[count - 1].get_width() - hero_move_right[step].get_width(), y, 60, 92) 
                else :
                    sword_rect = pygame.Rect(0,0,1,1)
            else :
                hero_rect = pygame.Rect(x + hero_walk_right[count].get_width() - 53, y, 53, 92)
        ghosts.draw(sc)
    # обработка результата текущего забега и выведение его в левый верхний угол
    sc_text = font.render(str(game_score), 1, (94, 138, 14))
    sc.blit(sc_text, (20, 10))

    #отображение призраков на экране и обновление экрана
    pygame.display.update()

    # фиксация FPS для большей плавности процесса
    clock.tick(FPS)