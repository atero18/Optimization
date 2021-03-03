# -*- coding: utf-8 -*-
"""
Créé le Mar 29 19:55

@author: Tangi Tassin
"""

from voyageur_de_commerce import *

nbNoeuds = 150
nbBoucles = 5
n = np.arange(10,nbNoeuds+1,10)
nomF = "tests/test_gurobi_" + str(nbNoeuds) + ".txt"
test_temporel_PL(nomF,n,nbBoucles,None, ['sc','MTZ'])