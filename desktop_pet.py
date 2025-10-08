import tkinter as tk
from turtle import title
from PIL import Image, ImageTk
import random
import os
import pygame
import ctypes
from ctypes import wintypes
import shutil

pygame.mixer.init()

class DesktopPet:
    def reset_action(self):
        self.moving = False
        self.running = False
        self.dancing = False
        self.sitting = False
        self.eating = False
        self.posing = False
        self.wiggling = False
        self.pirouetting = False
        self.becoming_dog = False
        self.hanging = False
        self.peacing = False
        self.eating_sprite_index = 0
        self.move_speed = 2
        self.move_delay = 50

    def __init__(self, window, sprites, title="Desktop Pet"):
        self.title = title
        self.window = window
        self.window.title(title)
        # Make window borderless, stay on top, and transparent
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True, '-transparentcolor', 'black')
        self.window.configure(bg='black')
        # Load sprites with transparency
        self.sprite_paths = sprites  # сохраняем пути для зеркалирования
        self.sprites = []
        for sprite in sprites:
            image = Image.open(sprite)
            image = image.resize((128, 128), Image.Resampling.LANCZOS)
            if image.mode != 'RGBA':
                image = image.convert('RGBA')
            self.sprites.append(ImageTk.PhotoImage(image))

        self.eating_sprites = []
        self.eating_sprite_index = 0
        if title == "Susie":  # Only for Susie pet
            try:
                # Load all 4 eating sprites
                for i in range(1, 5):
                    eat_image = Image.open(f'susie_eat/susie_eat{i}.png')
                    eat_image = eat_image.resize((128, 128), Image.Resampling.LANCZOS)
                    if eat_image.mode != 'RGBA':
                        eat_image = eat_image.convert('RGBA')
                    self.eating_sprites.append(ImageTk.PhotoImage(eat_image))
            except FileNotFoundError as e:
                print(f"Eating sprites not found: {e}, using default sprites")

        self.posing_sprite = None
        if title == "Susie":  # Only for Susie pet
            try:
                pose_image = Image.open('susie_pose.png')
                pose_image = pose_image.resize((128, 128), Image.Resampling.LANCZOS)
                if pose_image.mode != 'RGBA':
                    pose_image = pose_image.convert('RGBA')
                self.posing_sprite = ImageTk.PhotoImage(pose_image)
            except FileNotFoundError:
                print("susie_pose.png not found, using default sprites")
        if title == "Kris":  # Only for Kris pet
            try:   
                pose_image = Image.open('kris_pose.png')
                pose_image = pose_image.resize((128, 128), Image.Resampling.LANCZOS)
                if pose_image.mode != 'RGBA':
                    pose_image = pose_image.convert('RGBA')
                self.posing_sprite = ImageTk.PhotoImage(pose_image)
            except FileNotFoundError:
                print("kris_pose.png not found, using default sprites")

        self.becoming_dog_sprite = None
        if title == "Susie":  # Only for Susie pet
            try:
                become_dog_image = Image.open('susie_become_dog.png')
                become_dog_image = become_dog_image.resize((110, 110), Image.Resampling.LANCZOS)
                if become_dog_image.mode != 'RGBA':
                    become_dog_image = become_dog_image.convert('RGBA')
                self.becoming_dog_sprite = ImageTk.PhotoImage(become_dog_image)
            except FileNotFoundError:
                print("susie_dog.png not found, using default sprites")
        if title == "Kris":  # Only for Kris pet
            try:
                become_dog_image = Image.open('kris_become_dog.png')
                become_dog_image = become_dog_image.resize((110, 110), Image.Resampling.LANCZOS)
                if become_dog_image.mode != 'RGBA':
                    become_dog_image = become_dog_image.convert('RGBA')
                self.becoming_dog_sprite = ImageTk.PhotoImage(become_dog_image)
            except FileNotFoundError:
                print("kris_dog.png not found, using default sprites")          


        # Load sitting sprite if available
        self.sitting_sprite = None
        if title == "Kris":  # Only for Kris pet
            try:
                sit_image = Image.open('kris_sit.png')
                sit_image = sit_image.resize((110, 110), Image.Resampling.LANCZOS)
                if sit_image.mode != 'RGBA':
                    sit_image = sit_image.convert('RGBA')
                self.sitting_sprite = ImageTk.PhotoImage(sit_image)
            except FileNotFoundError:
                print("kris_sit.png not found, using default sprites")
        if title == "Susie":  # Only for Susie pet
            try:
                sit_image = Image.open('susie_sit.png')
                sit_image = sit_image.resize((128, 128), Image.Resampling.LANCZOS)
                if sit_image.mode != 'RGBA':
                    sit_image = sit_image.convert('RGBA')
                self.sitting_sprite = ImageTk.PhotoImage(sit_image)
            except FileNotFoundError:
                print("susie_sit.png not found, using default sprites")

        self.pirouetting_sprites = []
        self.pirouetting_sprite_index = 0
        if title == "Kris":  # Only for Kris pet
            try:
                # Load all pirouette sprites
                for i in range(1, 7):
                    ballet_image = Image.open(f'kris_ballet/kris_ballet{i}.png')
                    ballet_image = ballet_image.resize((128, 128), Image.Resampling.LANCZOS)
                    if ballet_image.mode != 'RGBA':
                        ballet_image = ballet_image.convert('RGBA')
                    self.pirouetting_sprites.append(ImageTk.PhotoImage(ballet_image))
            except FileNotFoundError as e:
                print(f"Pirouette sprites not found: {e}, using default sprites")

        self.wiggling_sprites = []
        self.wiggling_sprite_index = 0
        if title == "Kris":
            try:
                for i in range(1, 5):
                    wiggle_image = Image.open(f'kris_wiggle/kris_wiggle{i}.png')
                    wiggle_image = wiggle_image.resize((128, 128), Image.Resampling.LANCZOS)
                    if wiggle_image.mode != 'RGBA':
                        wiggle_image = wiggle_image.convert('RGBA')
                    self.wiggling_sprites.append(ImageTk.PhotoImage(wiggle_image))
            except FileNotFoundError as e:
                print(f"Wiggle sprites not found: {e}, using default sprites")


        self.hanging_sprites = []
        self.hanging_sprite_index = 0
        if title == "Kris":
            try:
                for i in range(1, 4):
                    hang_image = Image.open(f'kris_hang/kris_hang{i}.png')
                    hang_image = hang_image.resize((128, 128), Image.Resampling.LANCZOS)
                    if hang_image.mode != 'RGBA':
                        hang_image = hang_image.convert('RGBA')
                    self.hanging_sprites.append(ImageTk.PhotoImage(hang_image))
            except FileNotFoundError as e:
                print(f"Hanging sprites not found: {e}, using default sprites")

        self.peacing_sprite = None
        if title == "Kris":
            try:
                peace_image = Image.open('kris_peace.png')
                peace_image = peace_image.resize((128, 128), Image.Resampling.LANCZOS)
                if peace_image.mode != 'RGBA':
                    peace_image = peace_image.convert('RGBA')
                self.peacing_sprite = ImageTk.PhotoImage(peace_image)
            except FileNotFoundError:
                print("kris_peace.png not found, using default sprites")

        self.label = tk.Label(window, image=self.sprites[0], bg='black', bd=0)
        self.label.pack()
        # Initialize variables
        self.current_sprite = 0
        self.eating_sprite_index = 0
        self.moving = False
        self.direction = 1  # 1 for right, -1 for left
        self.running = False
        self.dancing = False
        self.sitting = False
        self.posing = False
        self.eating = False
        self.pirouetting = False
        self.wiggling = False
        self.becoming_dog = False
        self.hanging = False
        self.peacing = False
         # Movement speed and delay
        self.move_speed = 2
        self.move_delay = 50
        
        # Window dimensions
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        
        # Set initial position (adjusted for 128px size)
        self.x = random.randint(0, self.screen_width - 128)
        self.y = random.randint(0, self.screen_height - 128)
        self.window.geometry(f'+{self.x}+{self.y}')
        
        # Bind mouse events
        self.label.bind('<Button-1>', self.start_drag)
        self.label.bind('<B1-Motion>', self.on_drag)
        self.label.bind('<ButtonRelease-1>', self.end_drag)
        self.label.bind('<Button-3>', self.show_menu)
        
       
        # Make window focusable for keyboard events
        self.window.focus_set()
        
        # Start animation
        self.animate()
        self.move()
    
    def start_drag(self, event):
        self.moving = False
        self.hanging = True
        self.x = event.x
        self.y = event.y
       
    def show_menu(self, event):
        menu = tk.Menu(self.window, tearoff=0)
        menu.add_command(label="Сидеть", command=self.sit)
        menu.add_command(label="Бежать", command=self.run)
        menu.add_command(label="Танцевать", command=self.dance)
        menu.add_command(label="Позировать", command=self.pose)
        menu.add_command(label="Гулять", command=self.walk)
        menu.add_command(label="Стать собакой", command=self.become_dog)
        if self.title == "Susie":
            menu.add_command(label="Есть", command=self.eat)
        if self.title == "Kris":
            menu.add_command(label="Сделать пируэт", command=self.pirouette)
            menu.add_command(label="Дрыгаться", command=self.wiggle)
            menu.add_command(label="Показать мир", command=self.peace)
        menu.add_separator()
        
       
        # menu.add_separator()
        menu.add_command(label="Выйти", command=self.quit_program)
        # Позиционируем меню над питомцем
        x = self.window.winfo_x() + event.x
        y = self.window.winfo_y() + event.y - 40  # чуть выше
        menu.tk_popup(x, y)

    def sit(self):
        print("Питомец сел!")
        self.moving = False
        self.dancing = False
        self.running = False
        self.sitting = True
        self.move_speed = 0
        self.move_delay = 50
        self.window.after(300000, self.reset_action)

    def run(self):
        print("Питомец бежит!")
        self.moving = True
        self.running = True
        self.dancing = False
        self.move_speed = 8  # ускорение
        self.move_delay = 20
        self.direction = 1
        self.window.after(3000, self.reset_action)

    def dance(self):
        print("Питомец танцует!")
        self.moving = True
        self.dancing = True
        self.running = False
        self.move_speed = 10
        self.move_delay = 30
        self.window.after(200000, self.reset_action)

    def pose(self):
        print("Питомец позирует!")
        self.moving = False
        self.dancing = False
        self.running = False
        self.sitting = False
        self.posing = True
        self.move_speed = 0
        self.window.after(3000, self.reset_action)

   
    def walk(self):
        print("Питомец гуляет!")
        self.moving = True
        self.running = False
        self.dancing = False
        self.move_speed = 2
        self.move_delay = 50
        self.direction = random.choice([-1, 1])
        self.window.after(5000, self.reset_action)

    

    def eat(self):
        print("Питомец ест!")
        self.moving = False
        self.dancing = False
        self.running = False
        self.eating = True
        self.move_speed = 0
        self.window.after(300000, self.reset_action)

    def drink(self):
        print("Питомец пьёт!")
        self.moving = False
        self.dancing = False
        self.running = False
        self.move_speed = 0
        self.window.after(3000, self.reset_action)

    def pirouette(self):
        print("Питомец делает пируэт!")
        self.moving = False
        self.dancing = False
        self.running = False
        self.sitting = False
        self.posing = False
        self.eating = False
        self.pirouetting = True
        self.move_speed = 0
        self.window.after(5000, self.reset_action)

    def wiggle(self):
        print("Питомец дрыгается!")
        self.moving = False
        self.dancing = False
        self.running = False
        self.sitting = False
        self.posing = False
        self.eating = False
        self.pirouetting = False 
        self.wiggling = True
        self.move_speed = 0 
        self.window.after(10000, self.reset_action)

    def become_dog(self):
        print("Питомец становится собакой!")
        self.moving = False
        self.dancing = False
        self.running = False
        self.sitting = False
        self.posing = False
        self.eating = False
        self.pirouetting = False 
        self.wiggling = False
        self.becoming_dog = True
        self.move_speed = 0 
        self.window.after(20000, self.reset_action)

    def hang(self):
        print("Питомец висит!")
        self.moving = False
        self.dancing = False
        self.running = False
        self.sitting = False
        self.posing = False
        self.eating = False
        self.pirouetting = False 
        self.wiggling = False
        self.becoming_dog = False
        self.hanging = True
        self.move_speed = 0 
        self.window.after(10000, self.reset_action)

    def peace(self):
        print("Питомец показывает мир!")
        self.moving = False
        self.dancing = False
        self.running = False
        self.sitting = False
        self.posing = False
        self.eating = False
        self.pirouetting = False 
        self.wiggling = False
        self.becoming_dog = False
        self.hanging = False
        self.peacing = True
        self.move_speed = 0 
        self.window.after(10000, self.reset_action)

    def on_drag(self, event):
        x = self.window.winfo_x() + event.x - self.x
        y = self.window.winfo_y() + event.y - self.y
        self.window.geometry(f'+{x}+{y}')
        self.hanging = True  
        
    def end_drag(self, event):
        self.hanging = False

    def quit_program(self):
        self.window.quit()
    
    def animate(self):
        # If sitting and has sitting sprite, use it
        if self.sitting and self.sitting_sprite:
            self.label.configure(image=self.sitting_sprite)
            self.label.image = self.sitting_sprite
        elif self.becoming_dog and self.becoming_dog_sprite:
            self.label.configure(image=self.becoming_dog_sprite)
            self.label.image = self.becoming_dog_sprite
        elif self.peacing and self.peacing_sprite:
            self.label.configure(image=self.peacing_sprite)
            self.label.image = self.peacing_sprite
        elif self.eating and self.eating_sprites:
            # Animate eating with all 4 sprites
            self.eating_sprite_index = (self.eating_sprite_index + 1) % len(self.eating_sprites)
            current_eating_sprite = self.eating_sprites[self.eating_sprite_index]
            self.label.configure(image=current_eating_sprite)
            self.label.image = current_eating_sprite
        elif self.pirouetting and self.pirouetting_sprites:
            # Animate pirouette with all ballet sprites
            self.pirouetting_sprite_index = (self.pirouetting_sprite_index + 1) % len(self.pirouetting_sprites)
            current_pirouetting_sprite = self.pirouetting_sprites[self.pirouetting_sprite_index]
            self.label.configure(image=current_pirouetting_sprite)
            self.label.image = current_pirouetting_sprite
        elif self.posing and self.posing_sprite:
            self.label.configure(image=self.posing_sprite)
            self.label.image = self.posing_sprite
        elif self.wiggling and self.wiggling_sprites:
            self.wiggling_sprite_index = (self.wiggling_sprite_index + 1) % len(self.wiggling_sprites)
            current_wiggling_sprite = self.wiggling_sprites[self.wiggling_sprite_index]
            self.label.configure(image=current_wiggling_sprite)
            self.label.image = current_wiggling_sprite
        elif self.hanging and self.hanging_sprites:
            self.hanging_sprite_index = (self.hanging_sprite_index + 1) % len(self.hanging_sprites)
            current_hanging_sprite = self.hanging_sprites[self.hanging_sprite_index]
            self.label.configure(image=current_hanging_sprite)
            self.label.image = current_hanging_sprite
        
        else:
            # Switch between sprites
            self.current_sprite = (self.current_sprite + 1) % len(self.sprites)
            # Отразить изображение, если идём вправо
            if self.direction == 1:
                from PIL import ImageOps
                sprite_path = self.sprite_paths[self.current_sprite]
                image = Image.open(sprite_path)
                image = image.resize((128, 128), Image.Resampling.LANCZOS)
                if image.mode != 'RGBA':
                    image = image.convert('RGBA')
                image = ImageOps.mirror(image)
                mirrored_sprite = ImageTk.PhotoImage(image)
                self.label.configure(image=mirrored_sprite)
                self.label.image = mirrored_sprite  # чтобы не удалялось GC
            else:
                self.label.configure(image=self.sprites[self.current_sprite])
                self.label.image = self.sprites[self.current_sprite]
        self.window.after(200, self.animate)  # Change sprite every 200ms
    
    def move(self):
        if not self.moving:
            # Randomly decide to start moving (если не сидит)
            if not self.running and not self.dancing and not self.sitting and not self.eating and not self.posing and not self.pirouetting and not self.wiggling and not self.becoming_dog and not self.hanging:
                self.moving = random.random() < 0.3
                if self.moving:
                    self.direction = random.choice([-1, 1])
                    self.move_speed = 2  # восстановить обычную скорость
        
        if self.moving:
            x = self.window.winfo_x()
            y = self.window.winfo_y()
            if self.dancing:
                # Хаотичное движение
                dx = random.randint(-self.move_speed, self.move_speed)
                dy = random.randint(-self.move_speed, self.move_speed)
                x += dx
                y += dy
            else:
                # Обычное или ускоренное движение
                x += self.move_speed * self.direction
            # Проверка границ
            x = max(0, min(x, self.screen_width - 128))
            y = max(0, min(y, self.screen_height - 128))
            self.window.geometry(f'+{x}+{y}')
            # Остановить если не run/dance
            if not self.running and not self.dancing and random.random() < 0.02:
                self.moving = False
        self.window.after(self.move_delay, self.move)

if __name__ == "__main__":
    root = tk.Tk()
    # Первый питомец (Крис) — сложная анимация ходьбы
    kris_sprites = [
        'kris1.png', 'kris2.png', 'kris3.png', 'kris4.png'
    ]
    pet_kris = DesktopPet(root, kris_sprites, title="Kris")

    # Второй питомец (Сьюзи) — сложная анимация ходьбы
    susie_sprites = [
        'susie1.png', 'susie2.png', 'susie3.png', 'susie4.png'
    ]
    root2 = tk.Toplevel(root)
    pet_susie = DesktopPet(root2, susie_sprites, title="Susie")
    root.mainloop()