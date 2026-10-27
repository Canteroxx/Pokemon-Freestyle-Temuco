import pygame
from src.settings import WIDTH, HEIGHT, GOLD, CREAM, CHARACTERS


class CharacterSelect:
    def __init__(self):
        self.selected = 0
        self.punki_unlocked = False

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return None

        if event.key in (
            pygame.K_LEFT,
            pygame.K_a,
            pygame.K_RIGHT,
            pygame.K_d
        ):
            self.selected = 1 - self.selected

        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
            name = CHARACTERS[self.selected]

            if name == "punki" and not self.punki_unlocked:
                return None

            return "menu"

        return None

    def draw(self, screen, text, fonts, player):
        text(
            "SELECCIONAR PERSONAJE",
            90,
            fonts["normal"],
            GOLD
        )

        name = CHARACTERS[self.selected]

        img = player.frame(name, scale=2)

        if name == "punki" and not self.punki_unlocked:
            img = self.make_shadow(img)

        screen.blit(
            img,
            img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        )

        if name == "punki" and not self.punki_unlocked:
            label = "◀   ??? - BLOQUEADO   ▶"
        else:
            label = f"◀   {name.upper()}   ▶"

        text(label, HEIGHT - 145, fonts["normal"], GOLD)

        text(
            "← → CAMBIAR   ·   ENTER CONFIRMAR   ·   ESC VOLVER",
            HEIGHT - 35,
            fonts["small"],
            CREAM
        )

    @staticmethod
    def make_shadow(sprite):
        shadow = sprite.copy()

        # Conserva la silueta y la transparencia
        shadow.fill(
            (45, 45, 50, 255),
            special_flags=pygame.BLEND_RGBA_MULT
        )

        return shadow
