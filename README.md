# Mi Pokémon

RPG 2D inspirado en los juegos clásicos de Pokémon, desarrollado en Python con Pygame. El objetivo es crear una versión propia con nuevas criaturas, movimientos, personajes, mapas, historia y mecánicas.

## Tecnologías

- **Python 3.11 o superior:** lenguaje principal.
- **Pygame:** gráficos 2D, teclado, animaciones, sonido y ventana del juego.
- **Zed:** editor de código.
- **JSON:** almacenamiento de datos de criaturas, movimientos, habilidades, objetos y entrenadores.
- **Git y GitHub:** control de versiones y colaboración entre integrantes.

## Requisitos

- Python instalado.
- Zed instalado.
- Pygame instalado en un entorno virtual.
- Git recomendado para trabajar en equipo.

## Instalación

### 1. Clonar el repositorio

Si el proyecto ya está en GitHub:

```bash
git clone URL_DEL_REPOSITORIO
cd NOMBRE_DEL_REPOSITORIO
```

Si todavía no tienes repositorio, crea una carpeta y ábrela en Zed.

### 2. Crear el entorno virtual

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

Si existe `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Si aún no existe:

```bash
python -m pip install pygame
```

Para guardar las dependencias instaladas:

```bash
python -m pip freeze > requirements.txt
```

### 4. Ejecutar el juego

Desde la raíz del proyecto, con el entorno virtual activado:

```bash
python main.py
```

En Linux también puedes utilizar `python3 main.py` si ese es el comando disponible en tu sistema.

## Estructura del proyecto

```text
mi_pokemon/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── game.py
│   ├── player.py
│   ├── map.py
│   ├── battle.py
│   ├── creatures.py
│   └── data_loader.py
├── data/
│   ├── species.json
│   ├── moves.json
│   ├── abilities.json
│   ├── items.json
│   └── trainers.json
├── assets/
│   ├── characters/
│   ├── creatures/
│   ├── maps/
│   ├── ui/
│   ├── music/
│   └── sounds/
├── tests/
└── docs/
```

Esta estructura es una propuesta inicial. Se adaptará a la estructura real del repositorio y a medida que se implementen los sistemas.

## Organización del código

- `main.py`: punto de entrada del juego.
- `src/game.py`: inicialización y ciclo principal.
- `src/player.py`: movimiento, animaciones y estado del jugador.
- `src/map.py`: mapas, colisiones y transiciones.
- `src/battle.py`: reglas y flujo de los combates.
- `src/creatures.py`: estadísticas, niveles y estado de las criaturas.
- `src/data_loader.py`: lectura y validación de los archivos JSON.
- `data/`: datos del juego separados de la lógica.
- `assets/`: sprites, mapas, sonidos y otros recursos.
- `tests/`: pruebas automatizadas.
- `docs/`: documentación de mecánicas, historia y decisiones técnicas.

## Convenciones de desarrollo

- Mantener los datos separados de la lógica del juego.
- Usar nombres descriptivos para variables, funciones y archivos.
- Evitar concentrar toda la lógica en `main.py`.
- Crear módulos independientes para los sistemas principales.
- Probar los cambios antes de integrarlos a la rama principal.
- No subir el entorno virtual `.venv` al repositorio.
- Mantener los recursos gráficos organizados y con nombres consistentes.

## Trabajo en equipo

1. Cada integrante trabaja en una tarea o rama específica.
2. Los cambios se guardan mediante commits pequeños y descriptivos.
3. Las funcionalidades se integran después de probarlas.
4. Los formatos de datos y las interfaces entre módulos se acuerdan antes de trabajar en paralelo.

## Estado del proyecto

**Etapa inicial:** organización del proyecto y preparación de los recursos.

Próximos objetivos:

- [ ] Inicializar la ventana del juego.
- [ ] Cargar los sprites de los personajes.
- [ ] Implementar movimiento y animaciones.
- [ ] Crear el primer mapa jugable.
- [ ] Añadir colisiones e interacciones.
- [ ] Definir los formatos de datos de las criaturas y movimientos.
- [ ] Implementar un combate básico.
- [ ] Añadir guardado y carga de partida.

## Recursos y propiedad intelectual

El proyecto busca crear una experiencia propia inspirada en los RPG de criaturas. Antes de distribuirlo públicamente, se revisarán los derechos aplicables a los nombres, diseños, sprites, música y otros recursos utilizados.
