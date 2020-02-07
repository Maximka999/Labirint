import pygame
import random


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1],
                      [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
                      [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1],
                      [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                      [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                      [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                      [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                      [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                      [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                      [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                      [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                      [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                      [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.board2 = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                      [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                      [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                      [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                      [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                      [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                      [1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                      [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
                      [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]]
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 30
        self.razmer = razmer
        self.naprav = naprav
        self.polozx = polozx
        self.polozy = polozy
        self.diamonds = diamonds
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.xren = xren
        self.game = game
        self.board = board
        self.boardnumber = boardnumber
        self.image = pygame.transform.scale(pygame.image.load("Flash.png").convert(), (30, 30))
        self.image2 = pygame.transform.scale(pygame.image.load("apple.png").convert(), (30, 30))
        self.image3 = pygame.transform.scale(pygame.image.load("labirint.png ").convert(), (600, 600))

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        if self.boardnumber == 1:
            self.board = self.board1
        elif self.boardnumber == 2:
            self.board = self.board2
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, pygame.Color('red'), (
                    self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                    self.cell_size), 1)
        for i in range(self.razmer):
            for j in range(self.razmer):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, pygame.Color('white'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size))
        if self.boardnumber == 1:
            self.polozx = 10
            self.polozy = 0
            screen.blit(self.image, (300, 0))
            screen.blit(self.image2, (180, 540))
            screen.blit(self.image2, (270, 90))
            screen.blit(self.image2, (360, 450))
            screen.blit(self.image2, (420, 90))
            screen.blit(self.image2, (240, 300))
        elif self.boardnumber == 2:
            self.polozx = 1
            self.polozy = 0
            screen.blit(self.image, (30, 0))
            screen.blit(self.image2, (540, 90))
            screen.blit(self.image2, (90, 480))
            screen.blit(self.image2, (420, 150))
            screen.blit(self.image2, (30, 210))
            screen.blit(self.image2, (210, 210))

    def draw(self):
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont('areal', 30)
        chislo = int(pygame.time.get_ticks())
        stroka = ''
        chet = 0
        a = (chislo // 60000)
        b = ((chislo % 60000) // 1000)
        c = (((chislo % 60000) % 1000))
        if a == 0:
            a = ''
        else:
            a = str(a)
        if b == 0:
            b = ''
        else:
            b = str(b)
        if c == 0:
            c = ''
        else:
            c = str(c)

        while len(a) < 2:
            a = '0' + str(a)

        while len(b) < 2:
            b = '0' + str(b)

        while len(c) < 3:
            c = '0' + str(c)
        stroka = a + ':' + b + ',' + c
        text = font.render("Вы выиграли! " + "Ваше время - " + stroka, 1, (0, 0, 255))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 0, 255), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 3)
        self.game += 1

    def draw2(self):
        screen.blit(self.image3, (0, 0))
        font = pygame.font.SysFont('areal', 60)
        font1 = pygame.font.SysFont('areal', 50)
        text = pygame.transform.rotate(font.render("Дремучий лабиринт", 1, (0, 0, 0)), 19)
        text1 = font1.render("Уровень 1", 1, (86, 240, 226))
        text2 = font1.render("Уровень 2", 1, (86, 240, 226))
        screen.blit(text, (65, 50))
        screen.blit(text1, (210, 400))
        screen.blit(text2, (210, 475))

    def peremechenie(self, naprav):
        if self.boardnumber == 1 and self.game == 0:
            if self.polozx == 1 and self.polozy == 8 and self.xren == 0 and self.board[0][1] == 0:
                self.xren += 1
                self.board[6][1] = 1
                pygame.draw.line(screen, (0, 0, 0), (30, 180), (60, 210), 2)
                pygame.draw.line(screen, (0, 0, 0), (60, 180), (30, 210), 2)
                pygame.draw.rect(screen, pygame.Color('red'), (420, 510, 30, 30))
            if self.polozx == 14 and self.polozy == 17:
                pygame.draw.rect(screen, pygame.Color('white'), (30, 180, 30, 30))
                self.board[6][1] = 0
            if self.polozx == 2 and self.polozy == 18:
                screen.blit(self.image, (300, 0))
                pygame.draw.rect(screen, pygame.Color('white'), (2 * 30, 18 * 30, 30, 30))
                self.polozx = 10
                self.polozy = 0
            elif self.polozx == 12 and self.polozy == 17:
                screen.blit(self.image, (300, 0))
                pygame.draw.rect(screen, pygame.Color('white'), (12 * 30, 17 * 30, 30, 30))
                self.polozx = 10
                self.polozy = 0
            elif self.polozx == 18 and self.polozy == 14:
                screen.blit(self.image, (30 * 7, 30 * 18))
                pygame.draw.rect(screen, pygame.Color('white'), (18 * 30, 14 * 30, 30, 30))
                self.polozx = 7
                self.polozy = 18
            elif self.polozx == 8 and self.polozy == 18 and naprav == 2:
                pygame.draw.rect(screen, pygame.Color('red'), (8 * 30, 19 * 30, 30, 30))
                pygame.draw.rect(screen, pygame.Color('black'), ((8 * 30) + 1, (19 * 30) + 1, 28, 28))
                pygame.draw.rect(screen, pygame.Color('white'), (1 * 30, 0 * 30, 30, 30))
                self.board[19][8] = 1
                self.board[0][1] = 0
        if self.boardnumber == 2 and self.game == 0:
            if self.polozx == 17 and self.polozy == 1 and self.xren == 0 and self.board[1][19] == 0:
                pygame.draw.line(screen, pygame.Color('black'), (540, 30), (570, 60), 2)
                pygame.draw.line(screen, pygame.Color('black'), (570, 30), (540, 60), 2)
                self.board[1][18] = 1
                self.xren += 1
                pygame.draw.rect(screen, (255, 0, 0), (210, 450, 30, 30))
            elif self.polozx == 7 and self.polozy == 15 and self.xren > 0:
                self.board[1][18] = 0
                pygame.draw.rect(screen, (255, 255, 255), (540, 30, 30, 30))
                pygame.draw.rect(screen, (0, 255, 0), (210, 450, 30, 30))
                pygame.draw.rect(screen, (0, 0, 255), (210, 480, 30, 30))
                self.polozy = 16
            elif self.polozx == 11 and self.polozy == 9:
                pygame.draw.rect(screen, pygame.Color('white'), (11 * 30, 9 * 30, 30, 30))
                screen.blit(self.image, (30, 0))
                self.polozx = 1
                self.polozy = 0

        if naprav == 1:
            if self.board[self.polozy - 1][self.polozx] == 0:
                pygame.draw.rect(screen, pygame.Color('white'), (self.polozx * 30, self.polozy * 30, 30, 30))
                screen.blit(self.image, (self.polozx * 30, (self.polozy - 1) * 30))
                self.polozy -= 1
                if self.polozx == 1 and self.polozy == 0 and self.diamonds == 5 and self.boardnumber == 1:
                    self.game += 1
                    board.draw()
        elif naprav == 2 and self.game == 0:
            if self.polozx == 18 and self.polozy == 18 and self.boardnumber == 2:
                self.board[19][18] = 1
                self.board[1][19] = 0
                pygame.draw.rect(screen, pygame.Color('white'), (19 * 30, 30, 30, 30))
                pygame.draw.rect(screen, pygame.Color('red'), (18 * 30, 19 * 30, 30, 30))
                pygame.draw.rect(screen, pygame.Color('black'), (18 * 30 + 1, 19 * 30 + 1, 28, 28))
            elif self.board[self.polozy + 1][self.polozx] == 0:
                pygame.draw.rect(screen, pygame.Color('white'), (self.polozx * 30, self.polozy * 30, 30, 30))
                screen.blit(self.image, (self.polozx * 30, (self.polozy + 1) * 30))
                if self.polozx == 14 and self.polozy == 17 and self.boardnumber == 1 and self.xren > 0:
                    pygame.draw.rect(screen, pygame.Color('green'), (420, 510, 30, 30))
                self.polozy += 1
        elif naprav == 3 and self.game == 0:
            if self.board[self.polozy][self.polozx - 1] == 0:
                pygame.draw.rect(screen, pygame.Color('white'), (self.polozx * 30, self.polozy * 30, 30, 30))
                screen.blit(self.image, ((self.polozx - 1) * 30, (self.polozy) * 30))
                self.polozx -= 1
        elif naprav == 4:
            if self.polozx == 19 and self.polozy == 1 and self.boardnumber == 2 and self.diamonds == 5:
                self.game += 1
                board.draw()
            elif self.board[self.polozy][self.polozx + 1] == 0:
                pygame.draw.rect(screen, pygame.Color('white'), (self.polozx * 30, self.polozy * 30, 30, 30))
                screen.blit(self.image, ((self.polozx + 1) * 30, (self.polozy) * 30))
                self.polozx += 1
        if self.boardnumber == 1:
            if self.polozx == 9 and self.polozy == 3 and self.a1 == 0:
                self.diamonds += 1
                self.a1 = 1
            if self.polozx == 14 and self.polozy == 3 and self.a2 == 0:
                self.diamonds += 1
                self.a2 = 1
            if self.polozx == 8 and self.polozy == 10 and self.a3 == 0:
                self.diamonds += 1
                self.a3 = 1
            if self.polozx == 12 and self.polozy == 15 and self.a4 == 0:
                self.diamonds += 1
                self.a4 = 1
            if self.polozx == 6 and self.polozy == 18 and self.a5 == 0:
                self.diamonds += 1
                self.a5 = 1
        elif self.boardnumber == 2:
            if self.polozx == 18 and self.polozy == 3 and self.a1 == 0:
                self.diamonds += 1
                self.a1 = 1
            if self.polozx == 14 and self.polozy == 5 and self.a2 == 0:
                self.diamonds += 1
                self.a2 = 1
            if self.polozx == 1 and self.polozy == 7 and self.a3 == 0:
                self.diamonds += 1
                self.a3 = 1
            if self.polozx == 7 and self.polozy == 7 and self.a4 == 0:
                self.diamonds += 1
                self.a4 = 1
            if self.polozx == 3 and self.polozy == 16 and self.a5 == 0:
                self.diamonds += 1
                self.a5 = 1
        pygame.display.flip()



pygame.init()
naprav = 0
xren = 0
polozx = 0
polozy = 0
razmer = 20
diamonds = 0
boardnumber = 0
board = []
game = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
pygame.display.flip()
board = Board(razmer, razmer)
board.draw2()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 210 <= x <= 410 and 400 <= y <= 450:
                screen.fill((0, 0, 0))
                board.boardnumber = 1
                board.render()
            elif 210 <= x <= 410 and 475 <= y <= 525:
                screen.fill((0, 0, 0))
                board.boardnumber = 2
                board.render()
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game == 0:
                if event.key == pygame.K_UP:
                    naprav = 1
                    board.peremechenie(naprav)
                elif event.key == pygame.K_DOWN:
                    naprav = 2
                    board.peremechenie(naprav)
                elif event.key == pygame.K_LEFT:
                    naprav = 3
                    board.peremechenie(naprav)
                elif event.key == pygame.K_RIGHT:
                    naprav = 4
                    board.peremechenie(naprav)
        pygame.display.flip()
pygame.quit()
