from curses import wrapper, curs_set
import time
import random

class Snake():
    def __init__(self, scr):
        self.scr = scr
        self.length = 4
        self.path = [(5,8),(5,7),(5,6),(5,5)]
        self.direction = 0

    def embiggen(self):
        self.length += 1
    
    def keep_size(self):
        self.path = self.path[0:self.length]
    
    def turn(self, arrow):
        if self.direction == 0 or self.direction == 2:
            if arrow == 258:
                self.direction = 1
            elif arrow == 259:
                self.direction = 3
        elif self.direction == 1 or self.direction == 3:
            if arrow == 260:
                self.direction = 2
            elif arrow == 261:
                self.direction = 0
    
    def move(self):
        if self.direction == 0:
            self.path = [(self.path[0][0], self.path[0][1] + 1)] + self.path
        if self.direction == 1:
            self.path = [(self.path[0][0] + 1, self.path[0][1])] + self.path
        if self.direction == 2:
            self.path = [(self.path[0][0], self.path[0][1] - 1)] + self.path
        if self.direction == 3:
            self.path = [(self.path[0][0] - 1, self.path[0][1])] + self.path


class Ball():
    def __init__(self, scr):
        self.position = (10,10)
        self.scr = scr

    def new_position(self, snake):
        while True:
            y, x = self.scr.getmaxyx()
            self.position = (random.randrange(y), random.randrange(x))
            if not self.position in snake.path:
                break

def main(stdscr):
    # Clear screen

    curs_set(0)
    stdscr.clear()
    
    snake = Snake(stdscr)
    ball = Ball(stdscr)

    while True:
        stdscr.nodelay(True)
        c = stdscr.getch()

        time.sleep(.1)
        if c:
            snake.turn(c)

        snake.move()
        if snake.path[0] == ball.position:
            snake.embiggen()
            ball.new_position(snake)

        snake.keep_size()

        stdscr.clear()
        for y, x in snake.path:
            stdscr.addstr(y, x, u'\u25AE')
        
        stdscr.addstr(ball.position[0], ball.position[1], u'\u25AE')
        if len(snake.path) != len(set(snake.path)):
            break

wrapper(main)