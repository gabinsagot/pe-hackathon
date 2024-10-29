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
#Dans l'hypothèse où les lettres sont des ndarray
num = np.array([[1, 0, 0], [1, 1, 1], [0, 1, 0]])
def sym1(lettre):
    return np.flip(lettre, axis = 0)

sym1(num)

# %%
F = RAW_SHAPES["F"]
F, symetrie1(F)
