import random

gridWidth = 20
gridHeight = 20
canvasWidth = 600
canvasHeight = 600
falling_boxes = []
NUM_ROWS = 20
NUM_COLS = 10

game_board = [[" " for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def setup():
    size(canvasWidth, canvasHeight)
    background(0, 0, 0)
    stroke(180)
    new_block = create_falling_box()
    falling_boxes.append(new_block)

class Block:
    def __init__(self, x, y, size, velocity, R, G, B):
        self.x = x
        self.y = y
        self.size = size
        self.velocity = velocity
        self.R = R
        self.G = G
        self.B = B
        self.bounce = False

    def display(self):
        fill(self.R, self.G, self.B)
        circle(self.x, self.y, self.size)

    def bounce_check(self):
        if self.y <= 0:
            self.bounce = False
        elif self.y >= canvasHeight - self.size / 2:
            self.bounce = True

    def bounce_update(self):
        if self.bounce:
            self.y -= self.velocity
        else:
            self.y += self.velocity

    def move(self):
        if self.bounce:
            self.bounce_update()
        else:
            self.y += self.velocity

    def update(self):
        self.bounce_check()
        self.move()

def random_color():
    colors = [
        (255, 51, 52),
        (12, 150, 228),
        (30, 183, 66),
        (246, 187, 0),
        (76, 0, 153),
        (255, 255, 255),
        (0, 0, 0)
    ]
    return random.choice(colors)

def create_falling_box():
    new_x = random.randint(0, canvasWidth - 20)
    new_color = random_color()
    return Block(new_x, canvasHeight - 20, 5, 2, *new_color)

def draw():
    background(0, 0, 0)
    for box in falling_boxes:
        box.display()
        box.update()
    
    if frameCount % 60 == 0:
        new_block = create_falling_box()
        falling_boxes.append(new_block)
