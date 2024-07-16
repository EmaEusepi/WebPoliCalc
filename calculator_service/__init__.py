import ctypes
import os

# carico la libreria shared
_lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "calculator.so"))

# definisco i prototipi delle funzioni
_lib.add.argtypes = (ctypes.c_double, ctypes.c_double)
_lib.add.restype = ctypes.c_double

_lib.subtract.argtypes = (ctypes.c_double, ctypes.c_double)
_lib.subtract.restype = ctypes.c_double

_lib.multiply.argtypes = (ctypes.c_double, ctypes.c_double)
_lib.multiply.restype = ctypes.c_double

_lib.divide.argtypes = (ctypes.c_double, ctypes.c_double)
_lib.divide.restype = ctypes.c_double

_lib.power.argtypes = (ctypes.c_double, ctypes.c_double)
_lib.power.restype = ctypes.c_double

_lib.square_root.argtypes = (ctypes.c_double,)
_lib.square_root.restype = ctypes.c_double

_lib.modulus.argtypes = (ctypes.c_double, ctypes.c_double)
_lib.modulus.restype = ctypes.c_double


# definisco delle funzioni wrapper per chiamare le funzioni c
def add(a, b):
    return _lib.add(a, b)


def subtract(a, b):
    return _lib.subtract(a, b)


def multiply(a, b):
    return _lib.multiply(a, b)


def divide(a, b):
    return _lib.divide(a, b)


def power(base, exp):
    return _lib.power(base, exp)


def square_root(num):
    return _lib.square_root(num)


def modulus(a, b):
    return _lib.modulus(a, b)
