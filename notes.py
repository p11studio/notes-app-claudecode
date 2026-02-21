#!/usr/bin/env python3
"""CLI de notas - Gestiona tus notas desde la terminal."""

import argparse
import json
import sys
from pathlib import Path

NOTES_FILE = Path(__file__).parent / "notes.json"


def load_notes() -> list[dict]:
    """Carga las notas desde el archivo JSON."""
    if not NOTES_FILE.exists():
        return []
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_notes(notes: list[dict]) -> None:
    """Guarda las notas en el archivo JSON."""
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)


def add_note(text: str) -> None:
    """Agrega una nueva nota."""
    notes = load_notes()
    notes.append({"text": text})
    save_notes(notes)
    print(f"Nota agregada: {text}")


def list_notes() -> None:
    """Lista todas las notas."""
    notes = load_notes()
    if not notes:
        print("No hay notas guardadas.")
        return
    print("Notas:")
    for i, note in enumerate(notes, 1):
        print(f"  {i}. {note['text']}")


def delete_note(number: int) -> None:
    """Elimina una nota por su número."""
    notes = load_notes()
    if not notes:
        print("No hay notas para eliminar.")
        return
    if number < 1 or number > len(notes):
        print(f"Error: número inválido. Debe estar entre 1 y {len(notes)}.")
        sys.exit(1)
    removed = notes.pop(number - 1)
    save_notes(notes)
    print(f"Nota eliminada: {removed['text']}")


def search_notes(query: str) -> None:
    """Busca notas que contengan el texto especificado."""
    notes = load_notes()
    if not notes:
        print("No hay notas guardadas.")
        return
    results = [(i, n) for i, n in enumerate(notes, 1) if query.lower() in n["text"].lower()]
    if not results:
        print(f"No se encontraron notas con '{query}'.")
        return
    print(f"Resultados para '{query}':")
    for i, note in results:
        print(f"  {i}. {note['text']}")


def main():
    parser = argparse.ArgumentParser(description="CLI de notas")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # Comando: add
    add_parser = subparsers.add_parser("add", help="Agregar una nota")
    add_parser.add_argument("text", help="Texto de la nota")

    # Comando: list
    subparsers.add_parser("list", help="Listar todas las notas")

    # Comando: delete
    delete_parser = subparsers.add_parser("delete", help="Eliminar una nota por número")
    delete_parser.add_argument("number", type=int, help="Número de la nota a eliminar")

    # Comando: search
    search_parser = subparsers.add_parser("search", help="Buscar notas por texto")
    search_parser.add_argument("query", help="Texto a buscar")

    args = parser.parse_args()

    if args.command == "add":
        add_note(args.text)
    elif args.command == "list":
        list_notes()
    elif args.command == "delete":
        delete_note(args.number)
    elif args.command == "search":
        search_notes(args.query)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
