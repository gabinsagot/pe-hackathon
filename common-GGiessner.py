# Objectif de ma partie: 
# Prepare the exact_cover input: given a board and a set of pieces, compute the input to covers_bool()

# +
## information que j'ai au préalable
BOARD_6_10 = np.zeros((6, 10), dtype=DTYPE)
# # piece=?

## transformation des informations en quelque chose de compatible pour covers_bool()

def generate_matrix(tableau, dominos):
    rows = []
    for i in range(6):
        for j in range(10):
            for domino in dominos:
                # Vérifier si le domino peut être placé
                if can_place(domino, tableau, i, j):
                    row = [0] * (6 * 10)  # Taille du tableau
                    fill_row(row, domino, i, j)
                    rows.append(row)
    return rows

def can_place(domino, tableau, row, col):
    # Vérifier si le domino peut être placé dans le tableau
    if domino.dim<tabeau.dim:
    # Implémenter la logique de vérification ici
    pass

def fill_row(row, domino, row_start, col_start):
    # Remplir la ligne de la matrice pour le domino placé
    # Implémenter la logique ici
    pass


## Execution de la fonction exact-cover ou cover-bools
matrix = generate_matrix(tableau, dominos)
solutions = exact_cover(matrix)
for solution in solutions:
    print(solution)

## renvoit toutes les solutions permettant de compléter le tableau (si elles exitent)   exact_cover(matrix)
## on récupère une réponse disant i oui ou non le plateau est remplit                   covers_bool(plateau)  

#def exact_cover(matrix):
#    # Implémentation de l'algorithme d'exact cover ici
#    pass

#def covers_bool(plateau):
#    # Vérification si toutes les cases sont couvertes
#    return all(all(cell == 1 for cell in row) for row in plateau)
