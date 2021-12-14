import random
import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 12
        self.height = 12
        self.color1 = arcade.color.GREEN
        self.color2 = arcade.color.DARK_GREEN
        self.body_size = 0
        self.body = []
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.speed = 5
        self.change_x = 0
        self.change_y = 0
        self.score = 0

    def eat(self):
        self.body_size += 2
        self.score += 1
    
    def eatGolabi(self):
        self.score += 2

    def eatZarar(self):
        self.score -= 1

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color1)
        
        for i, part in enumerate(self.body):
            if i % 2 == 0:
                arcade.draw_rectangle_filled(part[0] , part[1], self.width, self.height, self.color2)
            else:
                arcade.draw_rectangle_filled(part[0] , part[1], self.width, self.height, self.color1)
   
    def move(self):
        self.body.append([self.center_x , self.center_y])

        if len(self.body) >  self.body_size:
            self.body.pop(0)
        
        if self.change_x == -1:
            self.center_x -= self.speed
        elif self.change_x == 1:
             self.center_x += self.speed
        
        if self.change_y == -1:
             self.center_y -= self.speed
        elif self.change_y == 1:
            self.center_y += self.speed     


class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color = arcade.color.RED
        self.r = 8
        self.center_x = random.randint(10,SCREEN_WIDTH-10)
        self.center_y = random.randint(10,SCREEN_HEIGHT-100)
    
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)

class Golabi(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.degre = 45
        self.color = arcade.color.GREEN_YELLOW
        self.center_x = random.randint(3,SCREEN_WIDTH-3)
        self.center_y = random.randint(3,SCREEN_HEIGHT-10)
    
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color, self.degre )

class Zarar(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 12
        self.height = 12
        self.degre = 45
        self.color = arcade.color.BROWN_NOSE
        self.center_x = random.randint(3,SCREEN_WIDTH-3)
        self.center_y = random.randint(3,SCREEN_HEIGHT-10)
    
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color, self.degre )

class Game(arcade.Window): 
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH , height=SCREEN_WIDTH, title='Snake Game')
        arcade.set_background_color(arcade.color.SAND) 
        self.snake = Snake()
        self.food = Apple()
        self.golabi = Golabi()
        self.zarar = Zarar()
    
    def on_draw(self):       
        arcade.start_render()
        arcade.draw_text('(Start : Enter key)', 200, 488, arcade.color.BLACK, font_size=10,align='left')
         
        if (self.snake.center_x==0 or self.snake.center_x==SCREEN_WIDTH) or (self.snake.center_y==0) or (self.snake.center_y==SCREEN_HEIGHT):
            self.chekWall()
   
        if self.snake.score >=0:
            text = f"Score: {self.snake.score}"
            arcade.draw_text(text, 10, 480, arcade.color.BLACK, font_size=12,align='left')

            self.snake.draw()
            self.food.draw()
            self.golabi.draw()
            self.zarar.draw()
        else:
            arcade.draw_text("GAME OVER...!",-40, 290,arcade.color.RED,width=600,font_size=15,align='center')
        

    def on_update(self, delta_time: float):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat()
            self.food = Apple()
        
        elif arcade.check_for_collision(self.snake, self.golabi):
            self.snake.eatGolabi()
            self.golabi = Golabi()

        elif arcade.check_for_collision(self.snake,self.zarar):
            self.snake.eatZarar()
            self.zarar = Zarar()
    
    def chekWall(self):

        if self.snake.center_x==0 :
            self.snake.change_x = 1
            self.snake.move()
            self.searchApple()

        elif self.snake.center_x==SCREEN_WIDTH:            
            self.snake.change_x = -1
            self.snake.move()
            self.searchApple()

        if self.snake.center_y==0:
            self.snake.change_y = 1
            self.snake.move()
            self.searchApple()

        elif self.snake.center_y==SCREEN_HEIGHT:
            self.snake.change_y = -1
            self.snake.move()
            self.searchApple()


    def searchApple(self):

        while self.food.center_x >= self.snake.center_x:
            self.snake.change_x = 1
            self.snake.change_y = 0
            self.snake.move()
            
            if self.food.center_y > self.snake.center_y:
                self.snake.change_y = 1
                self.snake.change_x = 0
                self.snake.move()

            elif self.food.center_y < self.snake.center_y:
                self.snake.change_y = -1
                self.snake.change_x = 0
                self.snake.move()

        while self.food.center_x <= self.snake.center_x:
            self.snake.change_x = -1
            self.snake.change_y = 0
            self.snake.move()
            
            if self.food.center_y > self.snake.center_y:
                self.snake.change_y = 1
                self.snake.change_x = 0
                self.snake.move()
            
            elif self.food.center_y < self.snake.center_y:
                self.snake.change_y = -1
                self.snake.change_x = 0
                self.snake.move()

       
                   
    def on_key_release(self, key: int, modifiers: int):
            if key == arcade.key.ENTER:
                self.searchApple()


myGame = Game()

arcade.run()
