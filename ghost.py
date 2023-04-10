import pygame

# класс, характеризующий привидения: здесь представлены их объявление и функция обновления координаты(и 
# удаление при уходе за границы экрана)
class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, score, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 224))
        self.speed = speed
        self.score = score
        self.add(group)

    def update(self):
        if self.rect.x > 0 :
            self.rect.x -= self.speed
        else:
            self.kill()
