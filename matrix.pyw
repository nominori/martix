from pygame import *
import random
import ctypes


class MatrixLetters:
    def __init__(self, app):
        self.app = app
        # list of symbols with ASCII coding
        self.letters = [chr(int('0x0040', 16) + i) for i in range(1, 27)] + [chr(int('0x0030', 16) + i) for i in range(10)]
        self.font_size = 17  # size of symbols
        self.font = font.SysFont('ms mincho', self.font_size, bold=True)  # font
        self.columns = app.width // self.font_size
        self.drops = [1 for i in range(0, self.columns)]

    def draw(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            char_render = self.font.render(char, False, (30, 160, 40))  # color render
            pos = i * self.font_size, (self.drops[i] - 1) * self.font_size
            self.app.surface.blit(char_render, pos)
            if self.drops[i] * self.font_size > app.height and random.uniform(0, 1) > 0.975:
                self.drops[i] = 0
            self.drops[i] += 1


class MatrixApp:
    def __init__(self):
        user32 = ctypes.windll.user32
        self.res = self.width, self.height = int(user32.GetSystemMetrics(0) / 1.2), int(user32.GetSystemMetrics(1) / 1.2)
        init()
        self.screen = display.set_mode(self.res)
        self.surface = Surface(self.res, SRCALPHA)
        self.clock = time.Clock()
        self.matrixLetters = MatrixLetters(self)

    def draw(self):
        while True:
            self.surface.fill((0, 0, 0, 10))  # color of background
            self.matrixLetters.draw()
            self.screen.blit(self.surface, (0, 0))
            [exit() for i in event.get() if i.type == QUIT]
            display.flip()
            self.clock.tick(35)  # falling speed of symbols


app = MatrixApp()
app.draw()
