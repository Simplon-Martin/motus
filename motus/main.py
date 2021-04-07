# exercice le Motus
import random

mot_list = ['ACTEUR', 'AVIRON', 'BOXEUR', 'BRONZE', 'BUDGET', 'CARTON', 'CHAQUE', 'CHEVAL',
            'CIMENT', 'CLIENT', 'COMPTE', 'CONTRE', 'CUPIDE', 'DESIGN', 'DICTER', 'DOSAGE',
            'DOUCHE', 'DROITE', 'EXPORT', 'FLAQUE', 'FORAGE', 'GLAIVE', 'GRAINE', 'GROUPE',
            'JARDIN', 'JUNGLE', 'LUCIDE', 'MANCHE', 'MARQUE', 'MIRAGE', 'MOUCHE', 'NIVEAU',
            'NOVICE', 'OISEAU', 'PAQUET', 'PILOTE', 'PLANTE', 'POTEAU', 'PROJET', 'PUBLIC',
            'REGAIN', 'RYTHME', 'SATIRE', 'SENTIR', 'SIMPLE', 'SONGER', 'SOUPLE', 'SQUARE']

mot = random.choice(mot_list)


def pas_dans_mot(lettre):
    res = lettre.lower() + " "
    return res


def motus(mot):
    cpt = 0
    while cpt != 8:
        res = []
        mot_user = input("veuillez saisir un mot : ")
        mot_user = mot_user.upper()
        if len(mot_user) == 6:
            for i in range(6):
                if mot[i] == mot_user[i]:
                    res.append(mot_user[i] + "#")
                elif mot.find(mot_user[i]) != -1:
                    res.append(mot_user[i] + "?")
                else:
                    res.append(pas_dans_mot(mot_user[i]))
        else:
            print("................")
        cpt += 1
        if mot_user == mot:
            print("GAGNE")
            exit()
        for j in range(6):
            print(res[j], end=" ")
        print()


motus(mot)
