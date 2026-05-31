import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray, inner, cross
from numpy.linalg import norm
from constants import epsilon

def vec(A:ndarray, B:ndarray)->ndarray:
    return B-A

def are_aligned(A:ndarray, B:ndarray, C:ndarray)->bool:
    u, v = vec(A,B), vec(A,C) 
    return inner(u, v)/norm(u)/norm(v)<=epsilon

def are_coplanar(A, B, C, D):
    u, v, w = vec(A,B), vec(A,C), vec(A,D)
    cst = norm(u)*norm(v)*norm(w)
    return inner(w, cross(u, v))/cst <= epsilon



