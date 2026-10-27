from src.settings import HEIGHT, GOLD

def draw_settings(text, fonts):
    text('CONFIGURACIÓN', 190, fonts['big'], GOLD)
    text('PRÓXIMAMENTE', HEIGHT // 2, fonts['normal'])
    text('ESC VOLVER', HEIGHT - 35, fonts['small'])
