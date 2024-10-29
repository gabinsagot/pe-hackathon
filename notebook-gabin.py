# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import exact_cover_py as ex

# %%
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


# %%
def into_numpy(d) :
    L = {}
    for i,v in d.items() :
        L[i] = np.array(v)
    return L


# %%
Lettres = into_numpy(RAW_SHAPES)


# %%
#Dans l'hypothèse où les lettres sont des ndarray

def sym1(lettre):
    return np.flip(lettre, axis = 0)
def sym2(lettre):
    return np.flip(lettre, axis = 1)
def rot1(lettre):
    return np.rot90(lettre)
def rot2(lettre):
    return np.rot90(lettre, 3)


# %%
np.rot90(num), num, np.rot90(num, 3)


# %%
#Pour l'instant, il y a des répétitions. Je n'ai pas su les empêcher
def transformations(lettres):
    d = {}
    for lettre in lettres:
        array = lettres[lettre]
        L = [sym1(array), sym2(array), sym1(sym2(array)), 
             rot1(array), sym1(rot1(array)), sym2(rot1(array)), 
             rot2(array), sym1(rot2(array)), sym2(rot2(array))]
        d[lettre]= L
    return d


# %%
transformations(Lettres)

# %%
