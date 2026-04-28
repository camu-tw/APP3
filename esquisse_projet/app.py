from students import (
    create_student,
    list_students,
    find_student,
    update_student,
    delete_student,
)
from storage import load_students, save_students
from utils import export_csv


def main():
    """Point d'entrée du programme: menu simple en ligne de commande.

    Ce fichier sert d'exemple central pour montrer comment utiliser les
    fonctions du projet. Il est volontairement simple et commenté en français
    pour un usage pédagogique.
    """
    students = load_students()

    menu = (
        "\n--- Gestion Étudiants (esquisse) ---\n"
        "1. Lister tous les étudiants\n"
        "2. Ajouter un étudiant\n"
        "3. Rechercher un étudiant par ID\n"
        "4. Mettre à jour un étudiant\n"
        "5. Supprimer un étudiant\n"
        "6. Exporter en CSV\n"
        "0. Quitter\n"
    )

    while True:
        print(menu)
        choice = input("Choix > ").strip()

        if choice == "1":
            list_students(students)
        elif choice == "2":
            student = create_student()
            students.append(student)
            save_students(students)
            print("Étudiant ajouté.")
        elif choice == "3":
            sid = input("ID de l'étudiant à rechercher > ").strip()
            found = find_student(students, sid)
            if found:
                print(found)
            else:
                print("Aucun étudiant trouvé pour cet ID.")
        elif choice == "4":
            sid = input("ID de l'étudiant à modifier > ").strip()
            updated = update_student(students, sid)
            if updated:
                save_students(students)
                print("Étudiant mis à jour.")
            else:
                print("Mise à jour annulée ou étudiant introuvable.")
        elif choice == "5":
            sid = input("ID de l'étudiant à supprimer > ").strip()
            removed = delete_student(students, sid)
            if removed:
                save_students(students)
                print("Étudiant supprimé.")
            else:
                print("Suppression annulée ou étudiant introuvable.")
        elif choice == "6":
            path = input("Nom de fichier CSV (ex: export.csv) > ").strip()
            export_csv(students, path)
            print(f"Exporté vers {path}.")
        elif choice == "0":
            print("Au revoir.")
            break
        else:
            print("Choix invalide, réessayez.")


if __name__ == "__main__":
    main()
