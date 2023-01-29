from curses import wrapper, curs_set, KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN
import time
import random

class Snake():
    def __init__(self, scr):
        self.scr = scr
        self.length = 4
        self.path = [(5,8),(5,7),(5,6),(5,5)]
        self.direction = "RIGHT"

    def embiggen(self):
        self.length += 1
    
    def keep_size(self):
        self.path = self.path[0:self.length]

    def turn(self, arrow):

        if self.direction == "RIGHT" or self.direction == "LEFT":
            if arrow == KEY_DOWN:
                self.direction = "DOWN"
            elif arrow == KEY_UP:
                self.direction = "UP"
        elif self.direction == "DOWN" or self.direction == "UP":
            if arrow == KEY_LEFT:
                self.direction = "LEFT"
            elif arrow == KEY_RIGHT:
                self.direction = "RIGHT"
    
    def move(self):
        if self.direction == "RIGHT":
            self.path = [(self.path[0][0], self.path[0][1] + 1)] + self.path
        if self.direction == "DOWN":
            self.path = [(self.path[0][0] + 1, self.path[0][1])] + self.path
        if self.direction == "LEFT":
            self.path = [(self.path[0][0], self.path[0][1] - 1)] + self.path
        if self.direction == "UP":
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
        
        # Get input
        c = stdscr.getch()

        time.sleep(.1)
        if c:
            snake.turn(c)

        snake.move()
        
        # Make the snake longer if it touches the ball.
        # Move the ball to a new random location

        if snake.path[0] == ball.position:
            snake.embiggen()
            ball.new_position(snake)


        # Update snake path
        snake.keep_size()

        stdscr.clear()
        for y, x in snake.path:
            stdscr.addstr(y, x, u'\u25AE')
        
        stdscr.addstr(ball.position[0], ball.position[1], u'\u25AE')
        
        # Stop if the snake hits itself

        if len(snake.path) != len(set(snake.path)):
            break

wrapper(main)
