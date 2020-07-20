import pygame


class Player:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.vel = 5
        self.left, self.right, self.standing = False, False, True
        self.walk_count, self.idle_count = 0, 0
        self.sprite_path = 'sprites/demon/'
        self.char = pygame.image.load('sprites/demon/idle1.png')
        self.walkLeft, self.walkRight, self.idle = [], [], []
        for i in range(1, 7):
            self.walkRight.append(pygame.image.load(self.sprite_path + "walk"+str(i)+".png"))
            self.walkLeft.append(pygame.transform.flip(self.walkRight[i-1], True, False))
            if i % 2 == 0:
                self.idle.append(pygame.image.load(self.sprite_path + "idle" + str(i // 2) + ".png"))

    def draw(self, window):
        if self.walk_count + 1 >= 60:
            self.walk_count = 0
        if self.idle_count + 1 >= 45:
            self.idle_count = 0

        if not self.standing:
            if self.left:
                window.blit(self.walkLeft[self.walk_count // 10], (self.x - self.width, self.y))
                self.walk_count += 1
            elif self.right:
                window.blit(self.walkRight[self.walk_count // 10], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.left:
                flipped = pygame.transform.flip(self.idle[self.idle_count // 15], True, False)
                window.blit(flipped, (self.x - self.width, self.y))
            else:
                window.blit(self.idle[self.idle_count // 15], (self.x, self.y))
            self.idle_count += 1

    def check_action(self, keys, gameDisplay):
        if keys[pygame.K_LEFT] and self.x + self.width > self.vel:
            self.move_left()
            self.standing = False
        elif keys[pygame.K_RIGHT] and self.x + (self.width * 2) < gameDisplay.get_width() - self.vel:
            self.move_right()
            self.standing = False
        else:
            self.standing = True

    def move_left(self):
        self.x -= self.vel
        self.left = True
        self.right = False

    def move_right(self):
        self.x += self.vel
        self.left = False
        self.right = True
