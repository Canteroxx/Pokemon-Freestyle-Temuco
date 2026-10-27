import pygame
from src.settings import ROOT

class MusicManager:
    def __init__(self):
        self.current = None
        self.volume = 0.45
        self.available = pygame.mixer.get_init() is not None

    def play_menu(self):
        if not self.available:
            return
        folder = ROOT / 'assets' / 'audio' / 'music'
        path = next((folder / f for f in ('menu.m4a', 'menu.mp3', 'menu.wav') if (folder / f).is_file()), None)
        if path is None:
            return  # No music supplied yet; game remains playable.
        if self.current == path and pygame.mixer.music.get_busy():
            return
        try:
            pygame.mixer.music.load(str(path))
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play(-1)
            self.current = path
        except pygame.error as exc:
            print(f'No se pudo reproducir la música: {exc}')

    def stop(self):
        if self.available and self.current is not None:
            pygame.mixer.music.stop()
            self.current = None
