"""Gestion simple de persistance: lecture/écriture JSON.

Ce module crée un dossier `data` local et lit/écrit le fichier
`students.json` pour la persistance minimale utilisée par l'esquisse.
"""
import json
import os
from typing import List, Dict

_DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
_DATA_FILE = os.path.join(_DATA_DIR, "students.json")


def _ensure_data_file() -> None:
    os.makedirs(_DATA_DIR, exist_ok=True)
    if not os.path.exists(_DATA_FILE):
        with open(_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)


def load_students() -> List[Dict]:
    _ensure_data_file()
    with open(_DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_students(students: List[Dict]) -> None:
    _ensure_data_file()
    with open(_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)
