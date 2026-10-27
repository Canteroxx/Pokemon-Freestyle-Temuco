
import pygame

from src.settings import WIDTH, HEIGHT, FPS, TITLE, CREAM, DARK
from src.screens.main_menu import MainMenu
from src.screens.character_select import CharacterSelect
from src.screens.gallery import Gallery
from src.screens.settings_screen import draw_settings
from src.entities.player import Player
from src.progress import Progress
from src.world.overworld import Overworld
from src.audio.music import MusicManager


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.fonts = {
            "normal": pygame.font.SysFont("consolas", 30, bold=True),
            "small": pygame.font.SysFont("consolas", 20, bold=True),
            "big": pygame.font.SysFont("consolas", 68, bold=True),
        }

        self.running = True
        self.state = "menu"

        # Pantallas
        self.menu = MainMenu()
        self.menu.load_background()

        self.selection = CharacterSelect()
        self.gallery = Gallery()

        # Jugador y mapa
        self.player = Player()
        self.overworld = Overworld()

        # Progreso guardado
        self.progress = Progress()

        self.selection.punki_unlocked = self.progress.punki_unlocked
        self.gallery.punki_unlocked = self.progress.punki_unlocked

        # Música
        self.music = MusicManager()
        self.music.play_menu()

        # Notificación de logro
        self.achievement_timer = 0.0

    def text(self, value, y, font=None, color=CREAM):
        surface = (font or self.fonts["normal"]).render(
            value,
            True,
            color
        )

        self.screen.blit(
            surface,
            surface.get_rect(center=(WIDTH // 2, y))
        )

    def change_state(self, state):
        previous = self.state
        self.state = state

        if state == "world":
            self.player.reset_position()
            self.overworld.reset()

            # Detener música del menú
            self.music.stop()

        elif state == "menu" and previous != "menu":
            self.music.play_menu()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if self.state != "menu":
                    self.change_state("menu")
                return

        action = None

        if self.state == "menu":
            action = self.menu.handle_event(event)

        elif self.state == "select":
            action = self.selection.handle_event(event)

        elif self.state == "gallery":
            action = self.gallery.handle_event(event)

        if action == "quit":
            self.running = False

        elif action:
            self.change_state(action)

    def update(self, dt):
        if self.achievement_timer > 0:
            self.achievement_timer = max(
                0.0,
                self.achievement_timer - dt
            )

        if self.state != "world":
            return

        # Movimiento
        self.player.update(dt)

        # Recoger manzanas
        completed = self.overworld.update(self.player)

        # Desbloquear a Punki una sola vez
        if completed and not self.progress.punki_unlocked:
            unlocked = self.progress.unlock_punki()

            if unlocked:
                self.selection.punki_unlocked = True
                self.gallery.punki_unlocked = True

                self.achievement_timer = 5.0

                print("LOGRO: Punki Negro desbloqueado")

    def draw_achievement(self):
        if self.achievement_timer <= 0:
            return

        rect = pygame.Rect(
            20,
            HEIGHT - 115,
            460,
            90
        )

        pygame.draw.rect(
            self.screen,
            (25, 30, 35),
            rect,
            border_radius=10
        )

        pygame.draw.rect(
            self.screen,
            (255, 195, 55),
            rect,
            width=3,
            border_radius=10
        )

        title = self.fonts["normal"].render(
            "LOGRO DESBLOQUEADO!",
            True,
            (255, 195, 55)
        )

        description = self.fonts["small"].render(
            "Punki Negro desbloqueado",
            True,
            (240, 240, 240)
        )

        self.screen.blit(
            title,
            (42, HEIGHT - 97)
        )

        self.screen.blit(
            description,
            (42, HEIGHT - 57)
        )

    def draw(self):
        self.screen.fill(DARK)

        if self.state == "menu":
            self.menu.draw(
                self.screen,
                self.text,
                self.fonts
            )

        elif self.state == "select":
            self.selection.draw(
                self.screen,
                self.text,
                self.fonts,
                self.player
            )

        elif self.state == "gallery":
            self.gallery.draw(
                self.screen,
                self.text,
                self.fonts,
                self.player
            )

        elif self.state == "settings":
            draw_settings(
                self.text,
                self.fonts
            )

        elif self.state == "world":
            character = getattr(
                self.selection,
                "character",
                "kankin"
            )

            # Impedir usar a Punki bloqueado
            if character == "punki" and not self.progress.punki_unlocked:
                character = "kankin"

            self.overworld.draw(
                self.screen,
                self.text,
                self.fonts,
                self.player,
                character
            )

            self.draw_achievement()

        pygame.display.flip()

    def run(self):
        while self.running:
            dt = min(
                self.clock.tick(FPS) / 1000,
                0.05
            )

            for event in pygame.event.get():
                self.handle_event(event)

            self.update(dt)
            self.draw()

        pygame.quit()
