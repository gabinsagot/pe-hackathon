RAW_SHAPES = {
    "F": [[1, 1, 0], [0, 1, 1], [0, 1, 0]],
    "I": [[1, 1, 1, 1, 1]],
    "L": [[1, 0, 0, 0], [1, 1, 1, 1]],
    "N": [[1, 1, 0, 0], [0, 1, 1, 1]],
    "P": [[1, 1, 1], [1, 1, 0]],
    "T": [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
    "U": [[1, 1, 1], [1, 0, 1]],
    "V": [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
    "W": [[1, 0, 0], [1, 1, 0], [0, 1, 1]],
    "X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
    "Y": [[0, 1, 0, 0], [1, 1, 1, 1]],
    "Z": [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
}


import numpy as np


def into_numpy(d) :
    L = {}
    for i,v in d.items() :
        L[i] = np.array(v)
    return L


into_numpy(RAW_SHAPES)


# +
def emplacements_possibles(P,B) :
    placements = []
    for i in range(len(B)) :
        for j in range(len(B[0])) :
            if peut_placer(P,B,(i,j)) :
                placements.append(1)
            else :
                placements.append(0)
    return placements

def peut_placer(P,B,loc) :
    px,py = 0,0
    for i in range(len(P)):
        for j in range(len(P[i])) :
            if P[i][j] == 1 :
                px = loc[0] + j 
                py = loc[1] + i
                if px < 0 or px > len(B) or py < 0 or py > len(B[0]) :
                    return False
    return True

# -






