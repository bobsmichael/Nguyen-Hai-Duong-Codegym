import tkinter as tk
import random
import pygame

WIDTH, HEIGHT = 400, 400
MOLE_SIZE = 50
GAME_TIME = 30

class WhackAMole:
    def __init__(self, root):
        self.root = root
        self.root.title("🐭 Whack-a-Mole Easy 🔨")

        pygame.mixer.init()
        self.hit_sound = pygame.mixer.Sound("hit.wav")
        self.miss_sound = pygame.mixer.Sound("miss.wav")

        self.score = 0
        self.time_left = GAME_TIME
        self.mole = None
        self.mole_type = "normal"

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="lightgreen")
        self.canvas.pack()

        self.score_label = tk.Label(root, text=f"Điểm: {self.score}", font=("Arial", 14))
        self.score_label.pack()

        self.time_label = tk.Label(root, text=f"Thời gian: {self.time_left}", font=("Arial", 14))
        self.time_label.pack()

        self.canvas.bind("<Button-1>", self.hit)

        self.update_timer()
        self.spawn_mole()

    def spawn_mole(self):
        if self.mole:
            self.canvas.delete(self.mole)

        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)

        if random.random() < 0.2:
            self.mole_type = "gold"
            color = "gold"
        else:
            self.mole_type = "normal"
            color = "brown"

        self.mole = self.canvas.create_oval(x, y, x + MOLE_SIZE, y + MOLE_SIZE, fill=color)

    def hit(self, event):
        if self.mole:
            x1, y1, x2, y2 = self.canvas.coords(self.mole)
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                if self.mole_type == "normal":
                    self.score += 1
                elif self.mole_type == "gold":
                    self.score += 3
                self.score_label.config(text=f"Điểm: {self.score}")
                pygame.mixer.Sound.play(self.hit_sound)
                self.spawn_mole()
            else:
                pygame.mixer.Sound.play(self.miss_sound)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Thời gian: {self.time_left}")
            self.root.after(1000, self.update_timer)
        else:
            self.canvas.delete("all")
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text=f"🎉 Hết giờ! Điểm: {self.score}", font=("Arial", 18), fill="red")

root = tk.Tk()
game = WhackAMole(root)
root.mainloop()