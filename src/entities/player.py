import pygame
from src.settings import ROOT, WIDTH, HEIGHT, CHARACTERS

class Player:
    def __init__(self):
        self.sheets = {}
        for name in CHARACTERS:
            path = ROOT / 'assets' / 'sprites' / 'characters' / f'{name}.png'
            self.sheets[name] = pygame.image.load(str(path)).convert_alpha()
        self.pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
        self.direction = 0
        self.anim = 0.0
        self.moving = False

    def reset_position(self):
        self.pos.update(WIDTH // 2, HEIGHT // 2)
        self.direction = 0
        self.anim = 0.0
        self.moving = False

    def frame(self, name, direction=0, index=0, scale=2):
        sheet = self.sheets[name]
        fw, fh = sheet.get_width() // 4, sheet.get_height() // 4
        rect = pygame.Rect((index % 4) * fw, (direction % 4) * fh, fw, fh)
        frame = sheet.subsurface(rect)
        return pygame.transform.scale(frame, (round(fw * scale), round(fh * scale)))

    def update(self, dt):
        keys = pygame.key.get_pressed()
        dx = int(keys[pygame.K_d] or keys[pygame.K_RIGHT]) - int(keys[pygame.K_a] or keys[pygame.K_LEFT])
        dy = int(keys[pygame.K_s] or keys[pygame.K_DOWN]) - int(keys[pygame.K_w] or keys[pygame.K_UP])
        delta = pygame.Vector2(dx, dy)
        self.moving = delta.length_squared() > 0
        if self.moving:
            delta.normalize_ip()
            self.pos += delta * 220 * dt
            self.pos.x = max(35, min(WIDTH - 35, self.pos.x))
            self.pos.y = max(100, min(HEIGHT - 15, self.pos.y))
            if abs(dx) > abs(dy):
                self.direction = 2 if dx > 0 else 1
            else:
                self.direction = 0 if dy > 0 else 3
            self.anim += dt * 8
        else:
            self.anim = 0.0
