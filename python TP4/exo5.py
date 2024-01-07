def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def est_date_valide(date):
    if len(date) > 8 or len(date) < 8:
        return 0

    jour = int(date[:2])
    mois = int(date[2:4])
    annee = int(date[4:])

    if mois < 1 or mois > 12:
        return False

    jours_par_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if est_bissextile(annee):
        jours_par_mois[2] = 29

    if jour < 1 or jour > jours_par_mois[mois]:
        return False

    return True

def main():
    date_saisie = input("Veuillez entrer une date au format jjmmaaaa : ")

    if est_date_valide(date_saisie):
        print("La date est valide.")
    else:
        print("La date est invalide.")

if __name__ == "__main__":
    main()