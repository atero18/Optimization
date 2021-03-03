# -*- coding: utf-8 -*-
"""
Créé le Apr 04 20:54

@author: Tangi Tassin
"""

from voyageur_de_commerce import *
nomF = "tests/test_constance_gurobi.txt"
open(nomF,'w').close()
n = [60]*200
test_temporel_PL(nomF,n,1,None, ["sc","MTZ"])