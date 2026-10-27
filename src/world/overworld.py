import pygame
from src.settings import WIDTH, HEIGHT, GOLD, CREAM


class Overworld:
    def __init__(self):
        self.apples = []
        self.collected = 0
        self.reset()

    def reset(self):
        self.apples = [
            pygame.Vector2(170, 160),
            pygame.Vector2(WIDTH - 170, 160),
            pygame.Vector2(170, HEIGHT - 130),
            pygame.Vector2(WIDTH - 170, HEIGHT - 130),
        ]

        self.collected = 0

    def update(self, player):
        player_rect = pygame.Rect(
            int(player.pos.x - 20),
            int(player.pos.y - 25),
            40,
            50
        )

        for apple in self.apples[:]:
            apple_rect = pygame.Rect(
                int(apple.x - 13),
                int(apple.y - 13),
                26,
                26
            )

            if player_rect.colliderect(apple_rect):
                self.apples.remove(apple)
                self.collected += 1

        return self.collected == 4

    def draw(self, screen, text, fonts, player, character):
        screen.fill((86, 151, 82))

        # Cuadrícula del mapa
        for x in range(0, WIDTH, 48):
            pygame.draw.line(
                screen, (73, 133, 71),
                (x, 0), (x, HEIGHT)
            )

        for y in range(0, HEIGHT, 48):
            pygame.draw.line(
                screen, (73, 133, 71),
                (0, y), (WIDTH, y)
            )

        # Manzanas
        for apple in self.apples:
            x, y = int(apple.x), int(apple.y)

            pygame.draw.circle(
                screen, (165, 30, 38), (x, y), 12
            )
            pygame.draw.circle(
                screen, (225, 65, 60), (x - 3, y - 3), 5
            )
            pygame.draw.line(
                screen, (80, 55, 25),
                (x, y - 10), (x + 2, y - 18), 3
            )
            pygame.draw.ellipse(
                screen, (50, 130, 45),
                (x + 2, y - 19, 11, 6)
            )

        # Personaje
        index = int(player.anim) % 4 if player.moving else 0

        sprite = player.frame(
            character,
            direction=player.direction,
            index=index,
            scale=1
        )

        screen.blit(
            sprite,
            sprite.get_rect(
                midbottom=(int(player.pos.x), int(player.pos.y))
            )
        )

        # Contador
        pygame.draw.rect(
            screen, (20, 45, 32),
            (18, 18, 235, 55),
            border_radius=8
        )

        text(
            f"MANZANAS: {self.collected}/4",
            35,
            fonts["small"],
            GOLD
        )
