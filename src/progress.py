import json
from src.settings import ROOT

SAVE_PATH = ROOT / "data" / "progress.json"


class Progress:
    def __init__(self):
        self.punki_unlocked = False
        self.load()

    def load(self):
        if not SAVE_PATH.exists():
            return

        try:
            with open(SAVE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.punki_unlocked = bool(
                data.get("punki_unlocked", False)
            )

        except (OSError, ValueError, TypeError):
            self.punki_unlocked = False

    def save(self):
        SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)

        with open(SAVE_PATH, "w", encoding="utf-8") as file:
            json.dump(
                {"punki_unlocked": self.punki_unlocked},
                file,
                indent=4
            )

    def unlock_punki(self):
        if self.punki_unlocked:
            return False

        self.punki_unlocked = True
        self.save()
        return True
