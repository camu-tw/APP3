"""Module `students` : contient le modèle et les opérations sur la liste
d'étudiants.

Toutes les fonctions utilisent des dictionnaires simples pour faciliter la
serialisation JSON et la compréhension pour des étudiants.
"""
from dataclasses import dataclass, asdict
import uuid
from typing import List, Dict, Optional


def _new_id() -> str:
    """Génère un identifiant unique simple."""
    return uuid.uuid4().hex[:8]


def create_student() -> Dict:
    """Crée un étudiant en interagissant avec l'utilisateur.

    Retourne un dictionnaire représentant l'étudiant.
    """
    print("--- Création d'un nouvel étudiant ---")
    first = input("Prénom > ").strip()
    last = input("Nom > ").strip()
    while True:
        grade_s = input("Note (0-20) > ").strip().replace(',', '.')
        try:
            grade = float(grade_s)
            if 0 <= grade <= 20:
                break
        except ValueError:
            pass
        print("Entrée invalide, renseignez un nombre entre 0 et 20.")

    student = {
        "id": _new_id(),
        "first_name": first,
        "last_name": last,
        "grade": grade,
    }
    return student


def list_students(students: List[Dict]) -> None:
    """Affiche la liste des étudiants de façon lisible."""
    if not students:
        print("Aucun étudiant enregistré.")
        return
    print("ID\tPrénom\tNom\tNote")
    for s in students:
        print(f"{s['id']}\t{s['first_name']}\t{s['last_name']}\t{s['grade']}")


def find_student(students: List[Dict], sid: str) -> Optional[Dict]:
    """Retourne l'étudiant correspondant à `sid` ou `None` si introuvable."""
    for s in students:
        if s.get("id") == sid:
            return s
    return None


def update_student(students: List[Dict], sid: str) -> bool:
    """Met à jour un étudiant. Retourne True si modifié."""
    s = find_student(students, sid)
    if not s:
        return False

    print("--- Mise à jour (laissez vide pour conserver) ---")
    first = input(f"Prénom [{s['first_name']}] > ").strip()
    last = input(f"Nom [{s['last_name']}] > ").strip()
    grade_s = input(f"Note [{s['grade']}] > ").strip().replace(',', '.')

    if first:
        s['first_name'] = first
    if last:
        s['last_name'] = last
    if grade_s:
        try:
            g = float(grade_s)
            if 0 <= g <= 20:
                s['grade'] = g
        except ValueError:
            pass
    return True


def delete_student(students: List[Dict], sid: str) -> bool:
    """Supprime l'étudiant par `sid`. Retourne True si supprimé."""
    for i, s in enumerate(students):
        if s.get('id') == sid:
            del students[i]
            return True
    return False
