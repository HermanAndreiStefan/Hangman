
def identificare_cuvant(cuvant_mascat, cuvant_complet, litere_de_verificat):
    cuvant_identificat = list(cuvant_mascat)
    incercari = 0
    litere_incercate = set(cuvant_mascat.replace('*', ''))  # Literele deja prezente în cuvantul mascat

    for litera in litere_de_verificat:
        if litera in litere_incercate:
            # Daca litera este deja în cuvantul mascat, o sarim
            continue

        gasit = False
        for i, char in enumerate(cuvant_complet):
            if char == litera and cuvant_identificat[i] == '*':
                cuvant_identificat[i] = litera
                gasit = True

        if gasit:
            print(f"Încercare {incercari + 1}: Litera '{litera}' găsită!")
        else:
            print(f"Încercare {incercari + 1}: Litera '{litera}' nu a fost găsită!")

        incercari += 1
        litere_incercate.add(litera)  # Adaugam litera la setul de litere încercate

        # Afisam progresul curent
        print(f"Stare curentă a cuvântului: {''.join(cuvant_identificat)}")

        # Daca am completat cuvantul, iesim din bucla
        if '*' not in cuvant_identificat:
            break

    return ''.join(cuvant_identificat), incercari


def procesare_fisier_txt(nume_fisier):
    total_incercari = 0
    litere_de_verificat = [
        'E', 'A', 'I', 'T', 'R', 'U', 'N', 'O', 'S', 'C', 'L', 'D', 'M', 'P', 'F', 'Î', 'V', 'B', 'G', 'H',
        'Ș', 'Ț', 'Z', 'Ă', 'Â', 'J', 'K', 'Q', 'W', 'X', 'Y'
    ]
    with open(nume_fisier, mode='r', encoding='utf-8') as file:
        for linie_numar, linie in enumerate(file, start=1):
            linie = linie.strip()
            if linie:  # Verificam dacă linia nu este goala
                try:
                    _, cuvant_mascat, cuvant_complet = linie.split(';')
                    cuvant_identificat, incercari = identificare_cuvant(cuvant_mascat, cuvant_complet,
                                                                        litere_de_verificat)

                    print(f"Cuvântul final pentru linia {linie_numar}: {cuvant_identificat}, încercări: {incercari}")
                    total_incercari += incercari
                except ValueError:
                    print(f"Linie incorectă la numărul {linie_numar}: {linie}")

    print(f"Total încercări pentru toate cuvintele: {total_incercari}")


if __name__ == "__main__":
    nume_fisier = 'cuvinte_de_verificat.txt'
    procesare_fisier_txt(nume_fisier)
