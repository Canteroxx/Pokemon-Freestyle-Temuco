# Pokémon Rap — versión con Punki oculto

## Instalación

```powershell
py -m pip install -r requirements.txt
py main.py
```

## Cambios
- Ventana 1280x720.
- Kankin es el único personaje jugable y seleccionable.
- Punki aparece en la galería como silueta gris oscura con nombre `???` y estado bloqueado.
- La imagen original de Punki permanece intacta; el efecto se aplica en memoria.
- Sprites 4x4 (256x320) cargados desde `assets/sprites/characters/`.
- Para cambiar el fondo del menú, pon tu PNG en `assets/backgrounds/menu.png`.
- Para música de menú, pon `menu.ogg` (o `menu.mp3`, `menu.wav`) en `assets/audio/music/`.
- Sin música ni fondo, el juego sigue funcionando con fondo verde y sin sonido.
- La música se detiene al entrar al mapa y vuelve al menú.

## Importante
No incluye una canción ni un fondo personalizados porque todavía no los has entregado.
Haz copia de seguridad de tu proyecto antes de reemplazar archivos.
