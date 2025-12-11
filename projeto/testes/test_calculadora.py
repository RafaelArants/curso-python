import pytest
from ferramentas.ferramentas import calcular

def test_soma():
    assert calcular(2,3,"soma") == "2 + 3 = 5"

def test_subtracao():
    assert calcular(2,3,"subtracao") == "2 - 3 = -1"

def test_multiplicacao():
    assert calcular(2,3,"multiplicacao") == "2 * 3 = 6"

# pytest -v