import pygame

pygame.init()
sc = pygame.display.set_mode((600, 360))

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

class Hero() :
    """основной герой"""
    speed = 6 # скорость персонажа
    jump_count = 8 # константа высоты прыжка персонажа
    x = 270 # начальное положение перонажа по оси Ox
    y = 264 # начальное положение персонажа по оси Oy
    rect_x = 270 # начальное положение react-a персонажа по оси Ox
    rect_y = 264 # начальное положение react-a персонажа по оси Oy
    count = 0 # показывает, какой номер изображения персонажа брять во время ходьбы
    step = 0 # показывает, какой номер изображения персонажа брять во время сложного движения
    is_jump = False # показывает, что персонаж в процессе полёта
    right = True # показывает, что персонаж смотрит вправо
    move = False # показывает, что персонаж в процессе выполнения сложного движения

    def __init__(self, surf) :
        self.image = surf
        self.hero_x = 270
        self.hero_y = 264

    def zeroing(self) :
        """возвращение элемента класса к начальным данным"""
        self.is_jump = False
        self.jump_count = 8
        self.x = 270
        self.y = 264
        self.rect_x = 270
        self.rect_y = 264
        self.move = False
        self.right = True
        self.count = 0
        self.step = 0

    def update(self, sc, game_stat) :
        """отслеживание перемещения, прыжков и ударов героя"""
        keys = pygame.key.get_pressed()
        if self.move and self.right and self.step != 0:
            self.rect_x = self.x
            self.rect_y = self.y - hero_move_right[self.step].get_height()
            sc.blit(hero_move_right[self.step], (self.x, self.y - hero_move_right[self.step].get_height()))
            self.step = (self.step + 1) % 5
            if self.step == 0 :
                self.move = False
        elif self.move and (not self.right) and self.step != 0 :
            self.rect_x = self.x
            self.rect_y = self.y - hero_move_right[self.step].get_height()
            sc.blit(hero_move_left[self.step], (self.x + hero_walk_right[self.count - 1].get_width() - hero_move_right[self.step].get_width(), self.y - hero_move_right[self.step].get_height()))
            self.step = (self.step + 1) % 5
            if self.step == 0 :
                self.move = False
        elif keys[pygame.K_a] and self.right:
            self.rect_x = self.x
            self.rect_y = self.y - hero_move_right[self.step].get_height()
            sc.blit(hero_move_right[self.step], (self.x, self.y - hero_move_right[self.step].get_height()))
            self.step = (self.step + 1) % 5
            self.move = True
        elif keys[pygame.K_a] :
            self.rect_x = self.x
            self.rect_y = self.y - hero_move_right[self.step].get_height()
            sc.blit(hero_move_left[self.step], (self.x + hero_walk_right[self.count - 1].get_width() - hero_move_right[self.step].get_width(), self.y - hero_move_right[self.step].get_height()))
            self.step = (self.step + 1) % 5
            self.move = True
        # обычное движение влево
        elif keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
            self.rect_x = self.x
            self.rect_y = self.y - hero_walk_right[self.count].get_height()
            self.count = (self.count + 1) % 6
            sc.blit(hero_walk_left[self.count], (self.x, self.y - hero_walk_right[self.count].get_height()))
            self.count = (self.count + 1) % 6
            self.right = False
        
        # обычное движение вправо
        elif keys[pygame.K_RIGHT] and self.x < 510:
            self.x += self.speed
            self.rect_x = self.x
            self.rect_y = self.y - hero_walk_right[self.count].get_height()
            sc.blit(hero_walk_right[self.count], (self.x, self.y - hero_walk_right[self.count].get_height()))
            self.count = (self.count + 1) % 6
            self.right = True
        # фиксированная стойка персонажа(смотрит влево или вправо)
        elif self.right: 
            self.rect_x = self.x
            self.rect_y = self.y - hero_walk_right[self.count].get_height()
            sc.blit(hero_walk_right[self.count], (self.x, self.y - hero_walk_right[self.count].get_height()))
        else : 
            self.rect_x = self.x
            self.rect_y = self.y - hero_walk_right[self.count].get_height()
            sc.blit(hero_walk_left[self.count], (self.x, self.y - hero_walk_right[self.count].get_height()))

        # выход в меню паузы
        if keys[pygame.K_ESCAPE] :
            game_stat.set_pause()
        # работа над прыжком 
        if not self.is_jump :
            if keys[pygame.K_SPACE] :
                self.is_jump = True
        else :
            if self.jump_count >= -8 :
                if self.jump_count > 0 :
                    self.rect_y -= (self.jump_count ** 2) / 2
                    self.y -= (self.jump_count ** 2) / 2
                else :
                    self.rect_y += (self.jump_count ** 2) / 2
                    self.y += (self.jump_count ** 2) / 2
                self.jump_count -= 1
            else :
                self.is_jump = False
                self.jump_count = 8
        # задание фиксированного прямоугольника, связанного с персонажем и его мечом, 
        # для фиксирования прохождения препятствий и убийства призраков
        if self.right : 
            self.rect = pygame.Rect(self.rect_x + 10, self.rect_y, 43, 92)
            if self.move and self.step > 1 and self.step < 4 :
                self.sword = pygame.Rect(self.rect_x + hero_move_right[self.step].get_width() - 60, self.rect_y, 60, 92) 
            else :
                self.sword = pygame.Rect(0,0,1,1) 
        else : 
            if self.move :
                self.rect = pygame.Rect(self.rect_x, self.rect_y, 53, 92)
                if self.step > 1 and self.step < 4 :
                    self.sword = pygame.Rect(self.rect_x + hero_walk_right[self.count - 1].get_width() - hero_move_right[self.step].get_width(), self.rect_y, 60, 92) 
                else :
                    self.sword = pygame.Rect(0,0,1,1)
            else :
                self.rect = pygame.Rect(self.rect_x + hero_walk_right[self.count].get_width() - 53, self.rect_y, 53, 92)

