import pygame


class Lines:
    # создание поля
    def __init__(self, width_, height_):
        self.width = width_
        self.height = height_
        self.board = [[0 for _ in range(width_)] for _ in range(height_)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.red = []

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen_):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if not self.board[i][j]:
                    pygame.draw.rect(screen_, 'black',
                                     [self.left + self.cell_size * j + 1, self.top + self.cell_size * i + 1,
                                      self.cell_size - 1, self.cell_size - 1])
                elif self.board[i][j] == 1:
                    pygame.draw.circle(screen_, 'blue',
                                       [self.left + self.cell_size * j + self.cell_size / 2,
                                        self.top + self.cell_size * i + self.cell_size / 2],
                                       self.cell_size / 2 - 2)
                elif self.board[i][j] == 2:
                    pygame.draw.circle(screen_, 'red',
                                       [self.left + self.cell_size * j + self.cell_size / 2,
                                        self.top + self.cell_size * i + self.cell_size / 2],
                                       self.cell_size / 2 - 2)
                pygame.draw.rect(screen_, 'white', [self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                    self.cell_size, self.cell_size], 1)

    def get_cell(self, mouse_pos: tuple):
        if (not self.left <= mouse_pos[0] <= self.left + self.cell_size * self.width or
                not self.top <= mouse_pos[1] <= self.top + self.cell_size * self.height):
            return None
        else:
            return (mouse_pos[1] - self.top) // self.cell_size, (mouse_pos[0] - self.left) // self.cell_size

    def on_click(self, cell, screen):
        if not self.board[cell[0]][cell[1]]:
            if not self.red:
                self.board[cell[0]][cell[1]] = 1
            else:
                if self.red[-1][0] == cell[0] and self.red[-1][-1] == cell[-1]:
                    self.board[cell[0]][cell[1]] = 1
                else:
                    if self.has_path(self.red[-1][0], self.red[-1][1], cell[0], cell[1]):
                        A = self.path(self.red[-1][0], self.red[-1][1], cell[0], cell[1])[::-1]
                        clock = pygame.time.Clock()
                        for i in range(len(A) - 2):
                            pygame.display.flip()
                            self.board[A[i][0]][A[i][1]] = 0
                            self.board[A[i + 1][0]][A[i + 1][1]] = 2
                            self.render(screen)
                            clock.tick(4)
                            pygame.display.flip()
                        self.board[A[-2][0]][A[-2][1]] = 0
                        self.board[A[-1][0]][A[-1][1]] = 1
                        clock.tick(4)
                        pygame.display.flip()
                        del self.red[0]
        elif self.board[cell[0]][cell[1]] == 1:
            self.board[cell[0]][cell[1]] = 2
            self.red.append([cell[0], cell[1]])
        else:
            self.board[cell[0]][cell[1]] = 1
            if [cell[0], cell[1]] in self.red:
                del self.red[-1]
        self.render(screen)

    def path(self, x1, y1, x2, y2):
        A = []
        INF = 1000
        x, y = x1, y1
        distance = [[INF] * self.width for _ in range(self.height)]
        distance[y][x] = 0
        prev = [[None] * self.width for _ in range(self.height)]
        queue = [(x, y)]
        while queue:
            x, y = queue.pop(0)
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                next_x, next_y = x + dx, y + dy
                if (0 <= next_x < self.width and 0 <= next_y < self.height and not self.board[next_x][next_y] and
                        distance[next_y][next_x] == INF):
                    distance[next_y][next_x] = distance[y][x] + 1
                    prev[next_y][next_x] = (x, y)
                    queue.append((next_x, next_y))
        x, y = x2, y2
        while prev[y][x] != (x1, y1):
            A.append((x, y))
            x, y = prev[y][x]
        return A + [(x, y)] + [(x1, y1)]

    def has_path(self, x1, y1, x2, y2):
        flag1 = False

        if x1 and y1 and not self.board[x1 - 1][y1 - 1]:
            flag1 = True

        elif x1 and not self.board[x1 - 1][y1]:
            flag1 = True

        elif x1 and y1 != self.width - 1 and not self.board[x1 - 1][y1 + 1]:
            flag1 = True

        elif y1 and not self.board[x1][y1 - 1]:
            flag1 = True

        elif y1 != self.width - 1 and not self.board[x1][y1 + 1]:
            flag1 = True

        elif x1 != self.height - 1 and y1 and not self.board[x1 + 1][y1 - 1]:
            flag1 = True

        elif x1 != self.height - 1 and not self.board[x1 + 1][y1]:
            flag1 = True

        elif x1 != self.height - 1 and y1 != self.width - 1 and not self.board[x1 + 1][y1 + 1]:
            flag1 = True

        flag2 = False

        if x2 and y2 and not self.board[x2 - 1][y2 - 1]:
            flag2 = True

        elif x2 and not self.board[x2 - 1][y2]:
            flag2 = True

        elif x2 and y2 != self.width - 1 and not self.board[x2 - 1][y2 + 1]:
            flag2 = True

        elif y2 and not self.board[x2][y2 - 1]:
            flag2 = True

        elif y2 != self.width - 1 and not self.board[x2][y2 + 1]:
            flag2 = True

        elif x2 != self.height - 1 and y2 and not self.board[x2 + 1][y2 - 1]:
            flag2 = True

        elif x2 != self.height - 1 and not self.board[x2 + 1][y2]:
            flag2 = True

        elif x2 != self.height - 1 and y2 != self.width - 1 and not self.board[x2 + 1][y2 + 1]:
            flag2 = True
        return flag1 and flag2

    def get_click(self, mouse_pos, screen):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell, screen)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 450, 450
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    pygame.display.set_caption('Линеечки')

    board = Lines(15, 15)
    board.set_view(0, 0, 30)
    running = True
    flag = False
    clock = pygame.time.Clock()
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos, screen)
                board.render(screen)
        board.render(screen)
        clock.tick(20)
        # обновление экрана
        pygame.display.flip()
    # завершение работы:
    pygame.quit()

