import pygame

class Statistic() :
    """статистика: лучший рекорд и последний результат"""
    def __init__(self, filename) :
        """открытие файла"""
        self.f = open(filename, 'r+')
        self.best_stata = int(self.f.readline())
        self.last_stata = int(self.f.readline())

    def __del__(self) :
        """закрытие файла"""
        self.f.close()

    def file_read(self, font, color) :
        """считывание статистики для отображения её в меню статистики"""
        best_stata = font.render('Лучший счёт' + str(self.best_stata), 1, color)
        last_stata = font.render('Последний счёт' +  str(self.last_stata), 1, color)
        return (best_stata, last_stata)
    
    def file_write(self, game_score) :
        """запись обновлённой статистики в файл"""
        self.best_stata = max(self.best_stata, game_score)
        self.last_stata = game_score
        self.f.seek(0)
        self.f.write(str(self.best_stata) + '\n')
        self.f.write(str(self.last_stata))

class GameState() :
    """основная игровая статистика"""
    def __init__(self) :
        self.pause = False #показывает, что сейчас пауза
        self.game = False #показывает, что сейчас игра активна
        self.begin = True #показывает, что сейчас начальное мнею
        self.settings = False #показывает, что сейчас меню настроек
        self.statistic = False #показывает,что сейчас меню статистики
        self.lose = False #показывает, что сейчас меню проигрыша
        self.game_score = 0 # показывает текущий рекорд персонажа за забег

    def get_stat(self) :
        """возвращает все элементы игровой статистики"""
        return (self.begin, self.lose, self.pause, self.settings, self.statistic, self.game)
    
    def get_score(self) :
        """возвращает текущий рекорд"""
        return self.game_score
    
    def add_score(self, score) :
        """меняет текущий рекорд"""
        self.game_score += score

    def set_stat(self) :
        """обнуляет все элементы игровой статистики"""
        self.pause = False
        self.game = False 
        self.begin = False 
        self.settings = False
        self.statistic = False
        self.lose = False

    def set_pause(self) :
        """переход в меню паузы"""
        self.set_stat()
        self.pause = True

    def set_game(self) :
        """переход в процесс игру"""
        self.set_stat()
        self.game = True

    def set_begin(self) :
        """переход в начальное меню"""
        self.set_stat()
        self.begin = True

    def set_settings(self) :
        """переход в меню настроек"""
        self.set_stat()
        self.settings = True

    def set_statistic(self) :
        """переход в меню статистики"""
        self.set_stat()
        self.statistic = True

    def set_lose(self) :
        """переход в меню поражения"""
        self.set_stat()
        self.lose = True