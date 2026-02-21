# Notes CLI

CLI de notas en Python para gestionar notas desde la terminal.

## Estructura

- `notes.py` - Script principal de la CLI
- `notes.json` - Archivo donde se persisten las notas (se genera automáticamente)

## Uso

```bash
python3 notes.py add "texto"      # Agregar nota
python3 notes.py list             # Listar notas
python3 notes.py delete <número>  # Eliminar nota por número
python3 notes.py search "texto"   # Buscar notas
```

## Tecnologías

- Python 3
- argparse (CLI)
- JSON (persistencia)
