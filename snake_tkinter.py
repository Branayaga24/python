import tkinter as tk
import random

# Game settings
WIDTH = 500
HEIGHT = 500
SNAKE_SIZE = 20
SPEED = 120   # lower = faster

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game - Tkinter")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.direction = "right"
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = None
        self.game_over_flag = False

        self.draw_snake()
        self.place_food()

        self.root.bind("<Key>", self.change_direction)
        self.move_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE,
                                         fill="green", tag="snake")

    def place_food(self):
        if self.food:
            self.canvas.delete(self.food)

        food_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        food_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

        self.food = self.canvas.create_oval(food_x, food_y,
                                            food_x + SNAKE_SIZE,
                                            food_y + SNAKE_SIZE,
                                            fill="red", tag="food")

        self.food_pos = (food_x, food_y)

    def change_direction(self, event):
        key = event.keysym

        if key == "Up" and self.direction != "down":
            self.direction = "up"
        elif key == "Down" and self.direction != "up":
            self.direction = "down"
        elif key == "Left" and self.direction != "right":
            self.direction = "left"
        elif key == "Right" and self.direction != "left":
            self.direction = "right"

    def move_snake(self):
        if self.game_over_flag:
            return

        x, y = self.snake[0]

        if self.direction == "right":
            x += SNAKE_SIZE
        elif self.direction == "left":
            x -= SNAKE_SIZE
        elif self.direction == "up":
            y -= SNAKE_SIZE
        elif self.direction == "down":
            y += SNAKE_SIZE

        new_head = (x, y)

        # Collision with walls
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            self.game_over()
            return

        # Collision with itself
        if new_head in self.snake:
            self.game_over()
            return

        self.snake.insert(0, new_head)

        # Check if food eaten
        if new_head == self.food_pos:
            self.place_food()
        else:
            self.snake.pop()

        self.draw_snake()
        self.root.after(SPEED, self.move_snake)

    def game_over(self):
        self.game_over_flag = True
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2,
                                text="GAME OVER",
                                fill="white",
                                font=("Arial", 24, "bold"))

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
