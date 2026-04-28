"""Utilitaires: export CSV et petites aides.
"""
import csv
from typing import List, Dict


def export_csv(students: List[Dict], path: str) -> None:
    """Exporte la liste d'étudiants vers un fichier CSV simple.

    Le format contient: id, first_name, last_name, grade
    """
    with open(path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "first_name", "last_name", "grade"]) 
        for s in students:
            writer.writerow([s.get("id"), s.get("first_name"), s.get("last_name"), s.get("grade")])
