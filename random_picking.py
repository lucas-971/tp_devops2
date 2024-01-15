import math

def proba_extraction(k, nb_rouge, nb_blanche, nb_noire):

    total_boules = nb_rouge + nb_blanche + nb_noire

    total_combinaisons = math.comb(total_boules, k)

    combinaisons_une_de_chaque = math.comb(nb_rouge, 1) * math.comb(nb_blanche, 1) * math.comb(nb_noire, 1)

    proba = combinaisons_une_de_chaque / total_combinaisons

    return proba

k = 5
nb_rouge = 3
nb_blanche = 1
nb_noire = 1

resultat = proba_extraction(k, nb_rouge, nb_blanche, nb_noire)
print(f"La probabilité d'obtenir exactement une boule de chaque couleur est : {resultat}")
