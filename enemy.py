import pygame

pygame.init()
sc = pygame.display.set_mode((600, 360))

class Ghost(pygame.sprite.Sprite):
    """обычное привидение"""
    count = 0
    image = pygame.image.load('images/ghost.png').convert_alpha()
    def __init__(self, x, speed, score, group):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect(center=(x, 224))
        if Ghost.count // 2 < 15 : # постепенное увеличение скорости призраков
            self.speed = speed + Ghost.count // 2
            Ghost.count += 1
        else : 
            self.speed = speed + 15
        self.score = score # количество очков, получаемых за убийство призрака
        self.add(group)

    @staticmethod
    def count_zeroing() :
        Ghost.count = 0

    def update(self):
        """проверка того, что призрак ушёл за границы экрана"""
        if self.rect.x > 0 :
            self.rect.x -= self.speed
        else:
            self.kill()
class OrangeGhost(Ghost):
    """оранжевый призрак"""
    image = pygame.image.load('images/orange_ghost.png').convert_alpha()
    def update(self):
        """проверка того, что призрак ушёл за границы экрана"""
        if self.rect.x < 600 :
            self.rect.x += self.speed
        else:
            self.kill()

def create_ghost(group):
    """создание обычного призрака"""
    x = 620
    speed = 4
    score = 1
    return Ghost(x, speed, score, group)

def create_orange_ghost(group):
    """создание оранжевого призрака"""
    x = -20
    speed = 6
    score = 1
    return OrangeGhost(x, speed, score, group)